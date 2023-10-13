#include "lists"

/**
 * print_dlistint - gsgsg
 * @h: fafasf
 * Return: afasf
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t ctr = 0;

	while (h)
	{
		printf("%d\n", h->n);
		h = h->next;
		ctr++;
	}

	return (ctr);
}
