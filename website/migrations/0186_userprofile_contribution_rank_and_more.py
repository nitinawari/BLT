# Generated by Django 5.1.4 on 2025-01-29 17:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0185_merge_20250126_1451"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="contribution_rank",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="merged_pr_count",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name="GitHubIssue",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("issue_id", models.IntegerField(unique=True)),
                ("title", models.CharField(max_length=255)),
                ("body", models.TextField(blank=True, null=True)),
                ("state", models.CharField(max_length=50)),
                (
                    "type",
                    models.CharField(
                        choices=[("issue", "Issue"), ("pull_request", "Pull Request")],
                        default="issue",
                        max_length=50,
                    ),
                ),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField()),
                ("closed_at", models.DateTimeField(blank=True, null=True)),
                ("merged_at", models.DateTimeField(blank=True, null=True)),
                ("is_merged", models.BooleanField(default=False)),
                ("url", models.URLField()),
                (
                    "repo",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="github_issues",
                        to="website.repo",
                    ),
                ),
                (
                    "user_profile",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="github_issues",
                        to="website.userprofile",
                    ),
                ),
            ],
        ),
    ]
