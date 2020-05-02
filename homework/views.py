# -*- coding: utf-8 -*-
from statistics import mean
from typing import List

from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(
            {
                'excellent_students': 'Student A, Student B',
                'bad_students': 'Student C, Student D'
            }
        )
        return context

class EntityGenerator:
    data = [
        {
            'id': 1,
            'fio': 'Someone',
            'timp': 2,
            'eis': 3,
            'philosophy': 4,
            'english': 5,
            'sport': 2.3
        },
        {
            'id': 2,
            'fio': 'Someone',
            'timp': 2,
            'eis': 3,
            'philosophy': 4,
            'english': 5,
            'sport': 2.3
        }
    ]

    def get_students(self):
        return [Student(e['fio']) for e in self.data]



class Student:
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

class Statistics:
    # student_id, [Scores]
    def __init__(self):
        self.stat = dict()

    def add_score(self, student, score):
        self.stat[student].append(score)
        self.stat[student] = self.stat.get(student, []).append(score)

    def get_scores(self, student):
        return self.stat.get(student, [])




class Subject:
    pass

class Score:
    # Subject, value
    def __init__(self, subject, value):
        self.subject = subject
        self.value = value
