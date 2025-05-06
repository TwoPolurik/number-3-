def sort_students_by_grade(students):
  """
  Сортирует список студентов по их баллам в порядке возрастания.

  Args:
    students: Список кортежей вида (имя, балл).

  Returns:
    Список кортежей, отсортированный по баллу (по возрастанию).
  """

  sorted_students = sorted(students, key=lambda student: student[1])
  return sorted_students

def print_sorted_students(sorted_students):
  """
  Выводит отсортированный список студентов.

  Args:
    sorted_students: Список кортежей, отсортированный по баллу (по возрастанию).
  """
  print("Студенты, отсортированные по баллам (по возрастанию):")
  for name, grade in sorted_students:
    print(f"Имя: {name}, Балл: {grade}")


# Пример использования
if __name__ == "__main__":
  students = [
      ("Алиса", 85),
      ("Боб", 70),
      ("Чарли", 92),
      ("Дэвид", 78),
      ("Ева", 98)
  ]

  sorted_students = sort_students_by_grade(students)
  print_sorted_students(sorted_students)

  # Дополнительные примеры использования (по желанию)
  print("\nТройка лидеров:")
  for name, grade in sorted_students[-3:]:
      print(f"Имя: {name}, Балл: {grade}")

  print("\nТройка отстающих:")
  for name, grade in sorted_students[:3]:
      print(f"Имя: {name}, Балл: {grade}")