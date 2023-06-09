#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 *
 * @head: Pointer to the head of the linked list.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	int list_size = 0;
	listint_t *current = *head;

	while (current != NULL)
	{
		list_size++;
		current = current->next;
	}
	int half_size = list_size / 2;
	int index;

	current = *head;
	for (index = 0; index < half_size; index++)
		current = current->next;
	listint_t *previous = NULL;
	listint_t *next_node = NULL;
	listint_t *second_half = current;

	while (current != NULL)
	{
		next_node = current->next;
		current->next = previous;
		previous = current;
		current = next_node;
	}
	listint_t *first_half = *head;

	second_half = previous;

	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
			return (0);
		first_half = first_half->next;
		second_half = second_half->next;
	}
	return (1);
}
