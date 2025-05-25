from django.core.management.base import BaseCommand
from skorlar.models import QuizQuestion

class Command(BaseCommand):
    help = 'Loads football quiz questions into the database'

    def handle(self, *args, **kwargs):
        QuizQuestion.objects.all().delete()

        # Quiz questions data with Turkish translations
        questions = [
            {
                'question': 'Which country has won the World Cup the most times?',
                'question_tr': 'Dünya Kupasını en çok hangi ülke kazandı?',
                'option_a': 'Brazil',
                'option_a_tr': 'Brezilya',
                'option_b': 'Germany',
                'option_b_tr': 'Almanya',
                'correct_answer': 'A'
            },
            {
                'question': 'How many players are on the field during a football match?',
                'question_tr': 'Bir futbol maçında sahada kaç oyuncu bulunur?',
                'option_a': '20',
                'option_a_tr': '20',
                'option_b': '22',
                'option_b_tr': '22',
                'correct_answer': 'B'
            },
            {
                'question': 'Which country is Lionel Messi from?',
                'question_tr': 'Lionel Messi hangi ülkedendir?',
                'option_a': 'Argentina',
                'option_a_tr': 'Arjantin',
                'option_b': 'Brazil',
                'option_b_tr': 'Brezilya',
                'correct_answer': 'A'
            },
            {
                'question': 'What does FIFA stand for?',
                'question_tr': 'FIFA\'nın açılımı nedir?',
                'option_a': 'Federation of International Football Athletes',
                'option_a_tr': 'Uluslararası Futbol Atletleri Federasyonu',
                'option_b': 'Fédération Internationale de Football Association',
                'option_b_tr': 'Uluslararası Futbol Federasyonları Birliği',
                'correct_answer': 'B'
            },
            {
                'question': 'In which year was the first FIFA World Cup held?',
                'question_tr': 'İlk FIFA Dünya Kupası hangi yıl düzenlendi?',
                'option_a': '1930',
                'option_a_tr': '1930',
                'option_b': '1950',
                'option_b_tr': '1950',
                'correct_answer': 'A'
            },
            {
                'question': 'Which club did Messi play for the longest?',
                'question_tr': 'Messi en uzun süre hangi kulüpte oynadı?',
                'option_a': 'Barcelona',
                'option_a_tr': 'Barcelona',
                'option_b': 'Real Madrid',
                'option_b_tr': 'Real Madrid',
                'correct_answer': 'A'
            },
            {
                'question': 'Where is Cristiano Ronaldo from?',
                'question_tr': 'Cristiano Ronaldo nerelidir?',
                'option_a': 'Portugal',
                'option_a_tr': 'Portekiz',
                'option_b': 'Italy',
                'option_b_tr': 'İtalya',
                'correct_answer': 'A'
            },
            {
                'question': 'What does "hat-trick" mean in football?',
                'question_tr': 'Futbolda "hat-trick" ne anlama gelir?',
                'option_a': 'A player receives 3 yellow cards',
                'option_a_tr': 'Bir oyuncunun 3 sarı kart görmesi',
                'option_b': 'A player scores three goals in a match',
                'option_b_tr': 'Bir oyuncunun bir maçta üç gol atması',
                'correct_answer': 'B'
            },
            {
                'question': 'What is the most prestigious club tournament in Europe?',
                'question_tr': 'Avrupa\'nın en prestijli kulüp turnuvası hangisidir?',
                'option_a': 'UEFA Europa League',
                'option_a_tr': 'UEFA Avrupa Ligi',
                'option_b': 'UEFA Champions League',
                'option_b_tr': 'UEFA Şampiyonlar Ligi',
                'correct_answer': 'B'
            },
            {
                'question': 'Who is the top goal scorer in football history?',
                'question_tr': 'Futbol tarihinin en golcü oyuncusu kimdir?',
                'option_a': 'Josef Bican',
                'option_a_tr': 'Josef Bican',
                'option_b': 'Cristiano Ronaldo',
                'option_b_tr': 'Cristiano Ronaldo',
                'correct_answer': 'A'
            }
        ]

        for question_data in questions:
            QuizQuestion.objects.create(**question_data)

        self.stdout.write(self.style.SUCCESS('Successfully loaded quiz questions')) 