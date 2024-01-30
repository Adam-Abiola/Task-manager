from django.test import TestCase, Client
from django.urls import reverse
from .models import Task


class TaskManagementTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.task_data = {'title': 'Test Task',
                          'description': 'This is a test task'}

    def test_create_task(self):
        # Assuming you have a 'create_task' URL in your app
        create_url = reverse('create_task')
        response = self.client.post(create_url, self.task_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Task.objects.filter(
            title=self.task_data['title']).exists())

    def test_update_task(self):
        task = Task.objects.create(
            title='Old Task', description='Old description')
        update_url = reverse('update_task', kwargs={'pk': task.pk})
        response = self.client.post(
            update_url, {'title': 'Updated Task'}, follow=True)
        self.assertEqual(response.status_code, 200)
        updated_task = Task.objects.get(pk=task.pk)
        self.assertEqual(updated_task.title, 'Updated Task')

    def test_delete_task(self):
        task = Task.objects.create(
            title='Task to delete', description='Delete me')
        delete_url = reverse('delete_task', kwargs={'pk': task.pk})
        response = self.client.post(delete_url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Task.objects.filter(pk=task.pk).exists())
