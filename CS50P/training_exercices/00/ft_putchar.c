#include <unistd.h>             /* j'inclue le header file (bibliothèque) unistd.h qui contient la fonction write */

void    ft_putchar(char c)      /*je crée une fonction sans valeur de retour (void: effectue une action mais ne retourne rien), et désigne une variable type char sur laquelle j'écris c.  ne pas oublier, pas d'espaces entre la fonction et le paramètre*/
{
        write(1, &c, 1);        /*1 est la sortie standard (cad le terminal), &c est l'adresse de c (la où est contenu le charactère), 1 signifie le nombre d'octets ici 1 seul où sera écrit c) [ le prototypage de write: ssize_t write(int fd, const void *buf, size_t count); ]*/
}


/* annotations par QuentinLACHENAL - 2024 */


/* zone de test*/

int	main()
{
	ft_putchar('a');
	return(0);
}
