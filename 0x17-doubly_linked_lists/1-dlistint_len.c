#include "lists.h"
/**
 * dlistint_len - returns the number of elements in a linked dlistint_t list.
 * @h: a pointer to the head node.
 *
 * Return: the number of elements in the linked dlistint_t list.
 */

size_t dlistint_len(const dlistint_t *h)
{
	size_t count = 1;
	const dlistint_t *tmp;

	while (h->next != NULL)
	{
		count = count + 1;
		tmp = h;
		h = tmp->next;
	}
	return (count);
}
