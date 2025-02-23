from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # Задаємо клас Meta, що відповідає за налаштування кастомізації форми
    class Meta:
        # Під'єднуємо модель пост до форми
        model = Post
        # Вказуємо назви рядків, які будемо відображати на сторінці форми
        fields = ['title', 'content', 'tags']
        # Кастомізація полів 
        widgets = {
            "title": forms.TextInput(
                attrs= {
                    'class': 'form-input',
                    'placeholder': 'Enter Title',
                    'id': 'title',
                }
            ),
            "content": forms.Textarea(
                attrs={
                    'class': 'content-input',
                    'placeholder': 'Enter Content',
                    'id': 'content'
                }
            )
        }
    # Перезаписуємо метод save 
    def save(self, author_profile):
        # Створюємо об'єкт поста за допомогою методу save
        # super().save(commit=False) - викликає базовий метод save з параметром commit=False    
        # але не зберігаємо у БД
        post: Post = super().save(commit=False)
        # Закріплюємо автора за створеним постом 
        post.author = author_profile
        post.save()
        # Встановлюємо теги для об'єкта пост 
        post.tags.set(self.cleaned_data.get('tags'))
        post.save()
    
