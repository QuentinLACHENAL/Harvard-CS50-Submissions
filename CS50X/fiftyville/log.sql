-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Find crime scene description --
SELECT description, year
FROM crime_scene_reports
WHERE month = 7 AND day = 28
AND street = 'Humphrey Street';
-- look at the interviews -- YEAR is 2024 --
SELECT name, id, transcript FROM interviews WHERE month = 7 anD day = 28 AND year = 2024;
--Ruth    | 161 | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
--If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
--| Eugene  | 162 | I don't know the thief's name, but it was someone I recognized. Earlier this morning,
--before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
--| Raymond | 163 | As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
-- In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
--The thief then asked the person on the other end of the phone to purchase the flight ticket.
-- look at bakery security logs -- IN THE bakERY -- theft was at 10:15 am -- (littering at 16:36)
-- !!! Ruth, Eugene and Raymond are witnesses -- RAYMOND says that the thief took money from the atm !!! thief had a car on the bakery parking.
SELECT hour, minute, activity, license_plate FROM bakery_security_logs WHERE year = 2024 AND month = 7 AND day = 28;
--| 10   | 8      | entrance | R3G7486       |
--| 10   | 14     | entrance | 13FNH73       |
--| 10   | 16     | exit     | 5P2BI95       |
--| 10   | 18     | exit     | 94KL13X       |
--| 10   | 18     | exit     | 6P58WS2       |
--| 10   | 19     | exit     | 4328GD8       |
--| 10   | 20     | exit     | G412CB7       |
--| 10   | 21     | exit     | L93JTIZ       |
--| 10   | 23     | exit     | 322W7JE       |
--| 10   | 23     | exit     | 0NTHK55       |
--| 10   | 35     | exit     | 1106N58       |
-- link it to names:
SELECT
    b.hour,
    b.minute,
    b.activity,
    b.license_plate,
    p.name AS owner_name
FROM bakery_security_logs AS b
JOIN people AS p ON b.license_plate = p.license_plate
WHERE b.year = 2024
  AND b.month = 7
  AND b.day = 28
  AND b. hour = 10;
---CHECK FOR PHONE CALLS
----+------+--------+----------+---------------+------------+
--| hour | minute | activity | license_plate | owner_name |
--+------+--------+----------+---------------+------------+
--| 10   | 8      | entrance | R3G7486       | Brandon    |
--| 10   | 14     | entrance | 13FNH73       | Sophia     |
--| 10   | 16     | exit     | 5P2BI95       | Vanessa    |
--| 10   | 18     | exit     | 94KL13X       | Bruce      |
--| 10   | 18     | exit     | 6P58WS2       | Barry      |
--| 10   | 19     | exit     | 4328GD8       | Luca       |
--| 10   | 20     | exit     | G412CB7       | Sofia      |
--| 10   | 21     | exit     | L93JTIZ       | Iman       |
--| 10   | 23     | exit     | 322W7JE       | Diana      |
--| 10   | 23     | exit     | 0NTHK55       | Kelsey     |
--| 10   | 35     | exit     | 1106N58       | Taylor     |
--| 10   | 42     | entrance | NRYN856       | Denise     |
--| 10   | 44     | entrance | WD5M8I6       | Thomas     |
--| 10   | 55     | entrance | V47T75I       | Jeremy     |
--+------+--------+----------+---------------+------------+
SELECT caller, receiver FROM phone_calls WHERE month = 7 anD day = 28 AND year = 2024 AND duration < 60;
--+----------------+----------------+
--|     caller     |    receiver    |
--+----------------+----------------+
--| (130) 555-0289 | (996) 555-8899 |
--| (499) 555-9472 | (892) 555-8872 |
--| (367) 555-5533 | (375) 555-8161 |
--| (499) 555-9472 | (717) 555-1342 |
--| (286) 555-6063 | (676) 555-6554 |
--| (770) 555-1861 | (725) 555-3243 |
--| (031) 555-6622 | (910) 555-3251 |
--| (826) 555-1652 | (066) 555-9701 |
--| (338) 555-6650 | (704) 555-2131 |
--+----------------+----------------+
SELECT name, phone_number FROM people;
-- Link it to names:
SELECT
    p1.name AS caller_name,
    p2.name AS receiver_name
FROM phone_calls
JOIN people AS p1 ON phone_calls.caller = p1.phone_number
JOIN people AS p2 ON phone_calls.receiver = p2.phone_number
WHERE phone_calls.month = 7
  AND phone_calls.day = 28
  AND phone_calls.year = 2024
  AND phone_calls.duration < 60;
--  +-------------+---------------+--
--| caller_name | receiver_name |
--+-------------+---------------+
--| Sofia       | Jack          |
--| Kelsey      | Larry         |
--| Bruce       | Robin         |
--| Kelsey      | Melissa       |
--| Taylor      | James         |
--| Diana       | Philip        |
--| Carina      | Jacqueline    |
--| Kenny       | Doris         |
--| Benista     | Anna          |
--
-- FIND NAMES FROM THE PEOPLE THAT WITHDRAWED MONEY FROM THE ATM:
SELECT
    atm.atm_location,
    atm.transaction_type,
    atm.account_number,
    atm.amount,
    p.name AS owner_name
FROM atm_transactions AS atm
JOIN bank_accounts AS ba ON atm.account_number = ba.account_number
JOIN people AS p ON ba.person_id = p.id
WHERE atm.year = 2024
  AND atm.month = 7
  AND atm.day = 28
  AND atm.atm_location LIKE 'Leggett Street';
--+----------------+------------------+----------------+--------+------------+
--|  atm_location  | transaction_type | account_number | amount | owner_name |
--+----------------+------------------+----------------+--------+------------+
--| Leggett Street | withdraw         | 49610011       | 50     | Bruce      |
--| Leggett Street | deposit          | 86363979       | 10     | Kaelyn     |
--| Leggett Street | withdraw         | 26013199       | 35     | Diana      |
--| Leggett Street | withdraw         | 16153065       | 80     | Brooke     |
--| Leggett Street | withdraw         | 28296815       | 20     | Kenny      |
--| Leggett Street | withdraw         | 25506511       | 20     | Iman       |
--| Leggett Street | withdraw         | 28500762       | 48     | Luca       |
--| Leggett Street | withdraw         | 76054385       | 60     | Taylor     |
--| Leggett Street | withdraw         | 81061156       | 30     | Benista    |
--+----------------+------------------+----------------+--------+------------+
-- LAST QUERY TO FIND THE SUSPECT
SELECT DISTINCT p.name
FROM people AS p
-- Join with bank accounts and ATM transactions
-- This finds people who used an ATM on Leggett Street
JOIN bank_accounts AS ba ON p.id = ba.person_id
JOIN atm_transactions AS atm ON ba.account_number = atm.account_number
WHERE atm.year = 2024
  AND atm.month = 7
  AND atm.day = 28
  AND atm.atm_location LIKE 'Leggett Street'
-- Check if the person made a short phone call
AND p.phone_number IN (
    SELECT DISTINCT phone_calls.caller
    FROM phone_calls
    JOIN people AS p1 ON phone_calls.caller = p1.phone_number
    JOIN people AS p2 ON phone_calls.receiver = p2.phone_number
    WHERE phone_calls.month = 7
      AND phone_calls.day = 28
      AND phone_calls.year = 2024
      AND phone_calls.duration < 60
)
-- Check if the person's car was in the bakery parking lot at 10:00
AND p.license_plate IN (
    SELECT DISTINCT b.license_plate
    FROM bakery_security_logs AS b
    JOIN people AS p ON b.license_plate = p.license_plate
    WHERE b.year = 2024
      AND b.month = 7
      AND b.day = 28
      AND b.hour = 10
);
--RESULT
--|  name  |
--+--------+
--| Bruce  |
--| Diana  |
--| Taylor |
--+--------+
-- SO I MUST CHECK FOR THE FLIGHTS:
SELECT f.id AS flight_id,
       a1.city AS origin_city,
       a2.city AS destination_city,
       f.year,
       f.month,
       f.day,
       f.hour,
       f.minute,
       p.name AS passenger_name
FROM flights AS f
JOIN airports AS a1 ON f.origin_airport_id = a1.id
JOIN airports AS a2 ON f.destination_airport_id = a2.id
JOIN passengers AS pa ON f.id = pa.flight_id
JOIN people AS p ON pa.passport_number = p.passport_number
WHERE f.year = 2024
  AND f.month = 7
  AND a1.city = 'Fiftyville'  -- Flight departs from Fiftyville
  AND p.name IN ('Bruce', 'Diana', 'Taylor')  -- Filtering by specific suspects
ORDER BY f.hour, f.minute;

---
--
--+-----------+-------------+------------------+------+-------+-----+------+--------+----------------+
--| flight_id | origin_city | destination_city | year | month | day | hour | minute | passenger_name |
--+-----------+-------------+------------------+------+-------+-----+------+--------+----------------+
--| 36        | Fiftyville  | New York City    | 2024 | 7     | 29  | 8    | 20     | Bruce          |
--| 36        | Fiftyville  | New York City    | 2024 | 7     | 29  | 8    | 20     | Taylor         |
--| 54        | Fiftyville  | Dallas           | 2024 | 7     | 30  | 10   | 19     | Diana          |
--| 18        | Fiftyville  | Boston           | 2024 | 7     | 29  | 16   | 0      | Diana          |
--+-----------+-------------+------------------+------+-------+-----+------+--------+----------------+
--
--WE FIND 2 SUSECTS: BRUCE and DIANA. How to know which one?
--"As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket."
--It was the earliest flight!! the first one is taken bu Bruce!!!
--BRUCE is the suspect.
--He called ROBIN
--HE WENT TO NYC
