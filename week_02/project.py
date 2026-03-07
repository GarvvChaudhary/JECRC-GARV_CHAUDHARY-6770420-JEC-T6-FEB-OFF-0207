import time

class TODO:
    # todos = [
    #     {'id': '',
    #      'desc': '',
    #      'is_completed': False
    #      }, {}, {}, {}
    # ]
    todos = []

    def add_todo(self, desc):
        ## 1. Take the desc from the user.
        ## 2. We have to create one dictionary in which we will add the todo desc.
        ## 3. We have to append that dictionary inside todos.
        if desc == '':
            print('Todo description cannot be empty.')
            return
        todo = {
            'id': int(time.time()),
            'desc': desc,
            'is_completed': False
        }
        self.todos.append(todo)
        print('Todo added successfully.')

    def remove_todo(self, id):
        for todo in self.todos:
            if todo['id'] == id:
                self.todos.remove(todo)
                print('Todo removed successfully.')
                return

        print('Todo not found.')

    def display_todos(self):
        todos = self.todos
        if not todos:
            print('No todos to display.')
            return
        for todo in todos:
            status = 'Completed' if todo['is_completed'] else 'Incomplete'
            print(f"ID: {todo['id']}, Description: {todo['desc']}, Status: {status}")
    
    def update_todo(self, id, new_desc):
        for todo in self.todos:
            if todo['id'] == id:
                todo['desc'] = new_desc
                print('Todo updated successfully.')
                return

        print('Todo not found.')
    
    def toggle_mark_as_completed(self, id):
        for todo in self.todos:
            if todo['id'] == id:
                todo['is_completed'] = not todo['is_completed']
                status = 'completed' if todo['is_completed'] else 'incomplete'
                print(f'Todo marked as {status}.')
                return

        print('Todo not found.')
    
    def completed_todos(self):
        completed = [todo for todo in self.todos if todo['is_completed']]
        if not completed:
            print('No completed todos to display.')
            return
        for todo in completed:
            print(f"ID: {todo['id']}, Description: {todo['desc']}")
    
    def incompleted_todos(self):
        
        incompleted = [todo for todo in self.todos if not todo['is_completed']]
        if not incompleted:
            print('No incomplete todos to display.')
            return
        for todo in incompleted:
            print(f"ID: {todo['id']}, Description: {todo['desc']}")

todo = TODO()
todo.add_todo('Take a Shower')
todo.add_todo('Clean the house')


todo.display_todos()
todo.toggle_mark_as_completed(todo.todos[0]['id'])
todo.display_todos()
todo.completed_todos()
todo.incompleted_todos()
todo.add_todo('Commit on GitHub')
todo.display_todos()
todo.update_todo(todo.todos[1]['id'], 'Clean the house and do the laundry')
todo.display_todos()
todo.remove_todo(todo.todos[0]['id'])
todo.display_todos()
todo.toggle_mark_as_completed(todo.todos[1]['id'])
todo.display_todos()