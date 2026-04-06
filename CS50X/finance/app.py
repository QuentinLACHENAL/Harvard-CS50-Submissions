import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
from datetime import datetime

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



@app.route("/")
@login_required
def index():
    """Display user's stock holdings and cash balance"""

    # get the user's ID from the session
    user_id = session["user_id"]

    # get the user's cash balance from the database
    user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

    # get a list of stocks the user owns (grouped by symbol and total shares)
    holdings = db.execute("""
        SELECT symbol, SUM(shares) AS total_shares
        FROM purchases
        WHERE user_id = ?
        GROUP BY symbol
    """, user_id)

    # create an empty list to store stock data (symbol, shares, price, total value)
    stock_data = []

    # start with the user's cash as the grand total
    grand_total = user_cash

    # go through each stock the user owns:
    for holding in holdings:
        symbol = holding["symbol"]
        total_shares = holding["total_shares"]

        # get the current price of the stock
        quote = lookup(symbol)

        # if the stock is not found, skip it and go to the next one
        if quote:
            price = quote["price"]
            total_value = price * total_shares

            # add the stock's total value to the grand total
            grand_total += total_value

            # add this stock's data to the stock_data list!!
            stock_data.append({
                "symbol": symbol,
                "total_shares": total_shares,
                "price": price,
                "total_value": total_value
            })

    # render the page and show the stock data, cash, and grand total.
    return render_template("index.html", stock_data=stock_data, user_cash=user_cash, grand_total=grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of a stock"""
    if request.method == "POST":
        # get form data
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # validate the symbol input
        if not symbol:
            return apology("must provide a stock symbol", 400)

        # check for the stock's price
        quote = lookup(symbol)
        if not quote:
            return apology(f"Could not find quote for {symbol}", 400)

        # validate shares input (must be a positive integer)
        try:
            shares = int(shares)
            if shares <= 0:
                return apology("must provide a positive number of shares", 400)
        except ValueError:
            return apology("shares must be a valid integer", 400)

        # get the user's cash balance
        user_id = session["user_id"]
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

        # calculate the cost (total) of the shares
        total_cost = quote["price"] * shares

        # check if user can afford the purchase
        if total_cost > user_cash:
            return apology("you do not have enough funds", 400)

        # deduct the cash from the user's balance
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_cost, user_id)

        # After a successful purchase, insert the stock purchase into purchases table
        # Check if the user already owns shares of the stock
        user_stock = db.execute("""
            SELECT * FROM purchases
            WHERE user_id = ? AND symbol = ?
        """, user_id, symbol)

        if len(user_stock) == 0:
            # if the user doesn't own this stock, insert a new row in purchases
            db.execute("""
            INSERT INTO purchases (user_id, symbol, shares, price)
            VALUES (?, ?, ?, ?)
            """, user_id, symbol, shares, quote["price"])
        else:
            # If the user already owns some shares, update the shares count
            db.execute("""
            UPDATE purchases
            SET shares = shares + ?
            WHERE user_id = ? AND symbol = ?
            """, shares, user_id, symbol)

        # Record the transaction in the transactions table
        db.execute("""
        INSERT INTO transactions (user_id, symbol, action, shares, price)
        VALUES (?, ?, 'BUY', ?, ?)
        """, user_id, symbol, shares, quote["price"])

        return redirect("/")

    # if GET, then we should render the buy form
    return render_template("buy.html")



@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]

    # retrieve all transactions for the user (buys and sells BOTH!!!)
    transactions = db.execute("""
        SELECT symbol, action, shares, price, timestamp
        FROM transactions
        WHERE user_id = ?
        ORDER BY timestamp DESC
    """, user_id)

    # render the transactions in a table:
    return render_template("history.html", transactions=transactions)



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        #get symbol
        symbol = request.form.get("symbol")

        #check if symbol exists
        if not symbol:
            return apology("You should provide a stock symbol", 400)
        #check the quote
        quote = lookup(symbol)

        #if quote is not an existing symbol then apology
        if not quote:
            return apology(f"I could not find quote for {symbol}", 400)

        return render_template("quoted.html", quote=quote)

    #if method = get
    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    #to clean the existing user session and start fresh
    session.clear()

    #check the method
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

    #validate that inputs are correct
        if not username:
            return apology("must provide username", 400)
        elif not password:
            return apology("must provide password", 400)
        elif not confirmation:
            return apology("must confirm password", 400)
        elif password != confirmation:
            return apology("passwords do not match", 400)

    #hash the pass
        hash_password = generate_password_hash(password)

        try:
            user_id = db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)", username, hash_password
            )
        except ValueError:
            return apology("Sorry, this login already exists.", 400)

        session["user_id"] = user_id

        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of a stock"""
    if request.method == "POST":
        # get form data
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # validate that a stock was selected
        if not symbol:
            return apology("must select a stock symbol", 400)

        # validate that shares input is a positive integer
        try:
            shares = int(shares)
            if shares <= 0:
                return apology("must provide a positive number of shares", 400)
        except ValueError:
            return apology("shares must be a valid integer", 400)

        # get user's ID and the amount of shares they own for the selected stock
        user_id = session["user_id"]
        user_shares = db.execute("""
            SELECT shares
            FROM purchases
            WHERE user_id = ? AND symbol = ?
        """, user_id, symbol)

        # check if user owns the stock and if they have enough shares
        if len(user_shares) == 0:
            return apology(f"You do not own any shares of {symbol}", 400)

        owned_shares = user_shares[0]["shares"]
        if shares > owned_shares:
            return apology(f"You do not own that many shares of {symbol}", 400)

        # get the current price of the stock
        quote = lookup(symbol)
        if not quote:
            return apology(f"Could not find quote for {symbol}", 400)

        price = quote["price"]
        total_sale_value = price * shares

        # update the user's cash balance by adding the sale value
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total_sale_value, user_id)

        # reduce the number of shares owned by the user (or remove the stock if no shares left)
        if shares == user_shares[0]["shares"]:
            db.execute("DELETE FROM purchases WHERE user_id = ? AND symbol = ?", user_id, symbol)
        else:
            db.execute("""
                UPDATE purchases
                SET shares = shares - ?
                WHERE user_id = ? AND symbol = ?
            """, shares, user_id, symbol)

        # log the transaction (sell action)
            db.execute("""
            INSERT INTO transactions (user_id, symbol, action, shares, price, timestamp)
            VALUES (?, ?, 'SELL', ?, ?, ?)
            """, user_id, symbol, shares, price, datetime.now())


        # redirect to home page after the sale is complete
        return redirect("/")

    # if GET request, render the sell form with a list of stocks the user owns
    user_id = session["user_id"]
    stocks = db.execute("""
        SELECT symbol
        FROM purchases
        WHERE user_id = ?
    """, user_id)

    return render_template("sell.html", stocks=stocks)

@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    """Allow users to change their password"""
    if request.method == "POST":
        # get the form data
        current_password = request.form.get("current_password")
        new_password = request.form.get("new_password")
        confirm_password = request.form.get("confirm_password")

        # ensure the current password is correct
        user_id = session["user_id"]
        user = db.execute("SELECT * FROM users WHERE id = ?", user_id)

        if len(user) != 1 or not check_password_hash(user[0]["hash"], current_password):
            return apology("Current password is incorrect", 400)

        # check if new password is valid
        if not new_password:
            return apology("New password cannot be empty", 400)

        # check new password and confirm password match
        if new_password != confirm_password:
            return apology("New passwords do not match", 400)

        # update the password
        hashed_password = generate_password_hash(new_password)
        db.execute("UPDATE users SET hash = ? WHERE id = ?", hashed_password, user_id)

        flash("Password changed successfully!")
        return redirect("/")

    # if GET request, render the password change form
    return render_template("change_password.html")


