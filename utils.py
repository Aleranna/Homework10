import json
from classes import Candidate


def load_candidates(file):
    """загружает данные из файла"""
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def get_all(candidates_list):
    """показывает всех кандидатов"""
    all_list = []
    for i in candidates_list:
        pk = i['pk']
        name = i['name']
        position = i['position']
        skills = i['skills']
        picture = i['picture']
        all_list.append(Candidate(pk, name, position, skills, picture))
    return all_list


def get_by_pk(pk, data):
    """возвращает кандидата по pk"""
    for i in data:
        if i.pk == pk:
            return i


def get_by_skill(skill_name, data):
    """возвращает кандидата по навыку"""
    candidates = []
    skill_name = skill_name.lower()
    for i in data:
        if skill_name in i.skills.strip().lower():
            candidates.append(i)
    return candidates














