
from education.models import CardOrdering
from education.models.user_education_status import UserEducationStatus, SemesterProgress

from education.constants import CARD_OBJ


class EducationService:

    def get_current_card_id(self, user):
        try:
            current_card_order_id = UserEducationStatus.objects.get(user=user).current_card
        except UserEducationStatus.DoesNotExist:
            current_card_order_id = 1
        return CardOrdering.objects.get(pk=current_card_order_id).pk

    def get_all_questions_by_card(self, request):
        card_id = self.get_current_card_id(user=request.user)
        card_type = CardOrdering.objects.get(pk=card_id).card_type
        current_level = SemesterProgress.objects.get(user=request.user).education_level
        data = {
            'questions': [],
            'card_type': card_type,
            'current_level': current_level
        }
        card_questions = CARD_OBJ.get(card_type).objects.get(pk=card_id).questions.all()
        for question in card_questions:
            answer_variants = question.answer_variants.values('id', 'name')
            data['questions'].append({
                'id': question.pk,
                'name': question.name,
                'answer_variants': answer_variants
            })
        return data

    def test_checker(self, user_result, user):
        mark = 0

        correct_result = self.get_questions_answers_by_card(user)

        for k, v in user_result.items():
            # TODO CODE 001 int type
            if correct_result.get(int(k)) == v:
                mark += 1
        return {
            'user': user,
            'mark': mark
        }

    def get_questions_answers_by_card(self, user):
        card_id = self.get_current_card_id(user=user)
        card_type = CardOrdering.objects.get(pk=card_id).card_type

        data = {}
        card_questions = CARD_OBJ.get(card_type).objects.get(pk=card_id).questions.all()
        for question in card_questions:
            correct_answer_variant = question.answer_variants.filter(is_correct=True).first().pk
            data[question.pk] = correct_answer_variant
        return data
