#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stddef.h>
/**
 * insert_node - fefef
 * @head: fasf
 * @number: fsfsd
 * Return: fasfsa
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *h = *head, *prev = *head, *node = NULL;

	node = malloc(sizeof(listint_t));
	if (!node || !number)
		return (NULL);

	node->n = number;

	if (!*head)
	{
		*head = node;
		return (node);
	}

	if (number < h->n)
	{
		node->next = h;
		return (*head = node);
	}

	while (h)
	{
		if (h->n > number)
		{
			node->next = h;
			prev->next = node;
			return (node);
		}
		prev = h;
		h = h->next;
	}
	node->next = h;
	prev->next = node;
	return (node);
}
