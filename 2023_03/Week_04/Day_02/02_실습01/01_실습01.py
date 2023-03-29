"""
1. 아래 할 일 생성
content : 실습 제출
priority : 5
completed : False
deadline : 오늘 날짜(년-월-일)
"""

# >>> from todos.models import Todo
# >>> from datetime import date
# >>> Todo.objects.create(content='실습 제출', priority=5, completed=False, deadline=date.today())
# <Todo: Todo object (1)>

""" 2. 아래 할 일 생성
content : 데일리 설문(오후) 제출
deadline : 오늘 날짜(년-월-일)
"""

# >>> Todo.objects.create(content='데일리 설문(오후) 제출', deadline=date.today())
# <Todo: Todo object (2)>

""" 
3. 임의의 할 일 5개 생성
"""

# >>> Todo.objects.create(content='과제 제출', priority=4, deadline=date.today())
# <Todo: Todo object (3)>
# >>> Todo.objects.create(content='수업 참석', priority=3)
# <Todo: Todo object (4)>
# >>> Todo.objects.create(content='과제 수행', priority=2)
# <Todo: Todo object (5)>
# >>> Todo.objects.create(content='과제 검토', priority=1)
# <Todo: Todo object (6)>
# >>> Todo.objects.create(content='과제 발표', deadline=date.today())
# <Todo: Todo object (7)>

""" 
4. pk 기준 오름차순으로 정렬한 모든 데이터 조회
"""

# >>> Todo.objects.all().order_by('pk')
# <QuerySet [<Todo: Todo object (1)>, <Todo: Todo object (2)>, <Todo: Todo object (3)>, <Todo: Todo object (4)>, <Todo: Todo object (5)>, <Todo: Todo object (6)>, <Todo: Todo object (7)>]>

""" 
5. priority 기준 내림차순으로 정렬한 모든 데이터 조회
"""

# >>> Todo.objects.all().order_by('-priority')
# <QuerySet [<Todo: Todo object (5)>, <Todo: Todo object (4)>, <Todo: Todo object (3)>, <Todo: Todo object (2)>, <Todo: Todo object (1)>, <Todo: Todo object (6)>, <Todo: Todo object (7)>]>

""" 
6. pk가 1인 단일 데이터의 아래 필드 조회
(pk, content, priority, deadline, created_at)
"""

# >>> todo = Todo.objects.get(pk=1)
# print(todo.pk, todo.content, todo.priority, todo.deadline, todo.created_at)
# 1 실습 3 2023-03-28 2023-03-28
