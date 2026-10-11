Коллекция Ansible my_own_namespace.yandex_cloud_elk

Коллекция содержит пользовательский модуль my_own_module для создания файла и роль my_own_role для запуска этого модуля.

Требования

- Ansible
- Python 3

Модуль my_own_module

Модуль создаёт файл и записывает в него заданное содержимое.

Параметры:

path - путь к файлу.
content - содержимое файла.

Пример использования модуля:

---
- name: Test custom module
  hosts: localhost
  connection: local
  tasks:
    - name: Create file
      my_own_namespace.yandex_cloud_elk.my_own_module:
        path: /tmp/test.txt
        content: "Hello Ansible"

Роль my_own_role

Роль расположена в roles/my_own_role/ и вызывает модуль my_own_namespace.yandex_cloud_elk.my_own_module.

Значения параметров по умолчанию находятся в roles/my_own_role/defaults/main.yml:

path: /tmp/test.txt
content: "Hello Ansible"

Задача роли находится в roles/my_own_role/tasks/main.yml:

---
- name: Create file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: "{{ path }}"
    content: "{{ content }}"

Пример playbook для запуска роли:

---
- name: Use custom role
  hosts: localhost
  connection: local
  roles:
    - my_own_namespace.yandex_cloud_elk.my_own_role

По умолчанию роль создаёт файл /tmp/test.txt с содержимым Hello Ansible.

Структура коллекции

plugins/modules/my_own_module.py — пользовательский модуль.
roles/my_own_role/defaults/main.yml — параметры по умолчанию.
roles/my_own_role/tasks/main.yml — задача, вызывающая модуль.
roles/my_own_role/ — роль.

