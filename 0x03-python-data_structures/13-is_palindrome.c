#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev_slow = NULL;
    listint_t *mid = NULL;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL) {
        return 1;
    }

    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;

        listint_t *temp = slow;
        slow = slow->next;
        temp->next = prev_slow;
        prev_slow = temp;
    }

    if (fast != NULL) {
        mid = slow;
        slow = slow->next;
    }

    while (slow != NULL) {
        if (slow->n != prev_slow->n) {
            is_palindrome = 0;
            break;
        }
        slow = slow->next;
        prev_slow = prev_slow->next;
    }

    while (prev_slow != NULL) {
        listint_t *temp = prev_slow->next;
        prev_slow->next = *head;
        *head = prev_slow;
        prev_slow = temp;
    }

    if (mid != NULL) {
        mid->next = *head;
        *head = mid;
    }

    return is_palindrome;
}
