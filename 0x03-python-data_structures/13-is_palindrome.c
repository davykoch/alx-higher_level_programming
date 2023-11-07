#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <stddef.h> /* Include the necessary header */

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the linked list
 */
void reverse_list(listint_t **head); /* Forward declaration */

/**
 * compare_lists - compares two linked lists
 * @list1: first linked list
 * @list2: second linked list
 * Return: 1 if the lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2); /* Forward declaration */

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 1 if it's a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *second_half = NULL;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;

        prev = slow;
        slow = slow->next;
    }

    if (fast != NULL)
    {
        slow = slow->next;
    }

    second_half = slow;
    prev->next = NULL;
    reverse_list(&second_half);

    is_palindrome = compare_lists(*head, second_half);

    reverse_list(&second_half);
    prev->next = second_half;

    return (is_palindrome);
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the linked list
 */
void reverse_list(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}

/**
 * compare_lists - compares two linked lists
 * @list1: first linked list
 * @list2: second linked list
 * Return: 1 if the lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
    while (list1 != NULL && list2 != NULL)
    {
        if (list1->n != list2->n)
            return (0);
        list1 = list1->next;
        list2 = list2->next;
    }

    return (list1 == NULL && list2 == NULL);
}
