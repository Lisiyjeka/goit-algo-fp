class ListNode:
    """Вузол однозв'язного списку"""
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def print_list(head):
    """Допоміжна функція для виведення списку"""
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

# 1. Функція реверсування однозв'язного списку
def reverse_linked_list(head):
    """Реверсує однозв'язний список, змінюючи посилання між вузлами"""
    prev = None
    current = head
    
    while current:
        next_node = current.next  # зберігаємо наступний вузол
        current.next = prev       # змінюємо посилання на попередній
        prev = current            # пересуваємо prev вперед
        current = next_node       # пересуваємо current вперед
    
    return prev  # новий початок списку

# 2. Алгоритм сортування для однозв'язного списку (сортування вставками)
def insertion_sort_linked_list(head):
    """Сортує однозв'язний список за допомогою сортування вставками"""
    if not head or not head.next:
        return head
    
    sorted_head = None  # голова відсортованого списку
    current = head
    
    while current:
        next_node = current.next  # зберігаємо наступний вузол для ітерації
        
        # Вставляємо поточний вузол у відсортований список
        if sorted_head is None or current.value < sorted_head.value:
            current.next = sorted_head
            sorted_head = current
        else:
            search = sorted_head
            # Шукаємо місце для вставки
            while search.next and search.next.value < current.value:
                search = search.next
            
            # Вставляємо вузол
            current.next = search.next
            search.next = current
        
        current = next_node
    
    return sorted_head

# 3. Функція об'єднання двох відсортованих списків
def merge_sorted_lists(list1, list2):
    """Об'єднує два відсортовані однозв'язні списки в один відсортований"""
    # Створюємо фіктивний початковий вузол для спрощення логіки
    dummy = ListNode()
    current = dummy
    
    # Порівнюємо вузли обох списків
    while list1 and list2:
        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Додаємо залишок першого або другого списку
    if list1:
        current.next = list1
    else:
        current.next = list2
    
    return dummy.next

# Допоміжна функція для створення списку з масиву
def create_linked_list(arr):
    """Створює однозв'язний список з масиву"""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    
    return head

# запуск тестів
if __name__ == "__main__":
    # Тестування реверсування
    print("1. Тестування реверсування списку:")
    list1 = create_linked_list([1, 2, 3, 4, 5])
    print("Оригінальний список:")
    print_list(list1)
    
    reversed_list = reverse_linked_list(list1)
    print("Реверсований список:")
    print_list(reversed_list)
    
    # Тестування сортування
    print("\n2. Тестування сортування списку:")
    list2 = create_linked_list([5, 2, 8, 1, 3])
    print("Несортований список:")
    print_list(list2)
    
    sorted_list = insertion_sort_linked_list(list2)
    print("Відсортований список:")
    print_list(sorted_list)
    
    # Тестування об'єднання
    print("\n3. Тестування об'єднання двох відсортованих списків:")
    list3 = create_linked_list([1, 3, 5])
    list4 = create_linked_list([2, 4, 6])
    print("Перший список:")
    print_list(list3)
    print("Другий список:")
    print_list(list4)
    
    merged_list = merge_sorted_lists(list3, list4)
    print("Об'єднаний відсортований список:")
    print_list(merged_list)