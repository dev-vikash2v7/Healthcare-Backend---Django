from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from authentication.models import UserProfile


class Command(BaseCommand):
    help = 'Create UserProfile for all users that don\'t have one'

    def handle(self, *args, **options):
        users_without_profile = []
        
        for user in User.objects.all():
            try:
                user.userprofile
            except UserProfile.DoesNotExist:
                users_without_profile.append(user)
        
        if not users_without_profile:
            self.stdout.write(
                self.style.SUCCESS('All users already have UserProfile objects.')
            )
            return
        
        self.stdout.write(f'Creating UserProfile for {len(users_without_profile)} users...')
        
        created_count = 0
        for user in users_without_profile:
            try:
                UserProfile.objects.create(user=user)
                created_count += 1
                self.stdout.write(f'Created UserProfile for user: {user.username}')
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Failed to create UserProfile for {user.username}: {e}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} UserProfile objects.')
        )
