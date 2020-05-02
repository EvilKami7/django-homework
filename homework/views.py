# -*- coding: utf-8 -*-
from copy import copy
from statistics import mean
from typing import List

from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        generator = EntityGenerator()
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'students_statistics': generator.get_statistics(),
                'excellent_students': generator.get_excellent_students(),
                'bad_students': generator.get_bad_students()
            }
        )
        return context

class EntityGenerator:
    data = [
        {
            'id': 1,
            'fio': 'Some Petr',
            'timp': 2,
            'eis': 3,
            'philosophy': 4,
            'english': 5,
            'sport': 2.3
        },
        {
            'id': 2,
            'fio': 'Some Ivan',
            'timp': 5,
            'eis': 5,
            'philosophy': 5,
            'english': 5,
            'sport': 5
        }
    ]

    def __init__(self):
        self.statistics = Statistics()
        for s_data in self.data:
            scores = [Score(key, value) for key, value in s_data.items() if key not in ('id', 'fio')]
            self.statistics.set_scores(Student(s_data['id'], s_data['fio']), scores)

    def get_students(self):
        return ', '.join(self.statistics.get_students())

    def get_statistics(self):
        for s_data in self.data:
            s_data['average'] = self.statistics.get_average_score(Student(s_data['id'], s_data['fio']))
        return self.data

    def get_excellent_students(self):
        return ', '.join(self.statistics.get_excellent())

    def get_bad_students(self):
        return ', '.join(self.statistics.get_bad())



class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __hash__(self):
        return self.id

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Student({self.name})'

class Statistics:
    # student_id, [Scores]
    def __init__(self):
        self.stat = dict()

    def set_scores(self, student, scores):
        self.stat[student] = scores

    def get_scores(self, student):
        return self.stat.get(student, [])

    def get_students(self):
        return self.stat.keys()

    def get_average_score(self, student):
        return mean([score.value for score in self.get_scores(student)])

    def get_excellent(self):
        return [student.name for student in self.stat.keys() if self.get_average_score(student) >= 4.5]

    def get_bad(self):
        return [student.name for student in self.stat.keys() if self.get_average_score(student) < 4]

class Score:
    # Subject, value
    def __init__(self, subject, value):
        self.subject = subject
        self.value = value
