import math


class University:
    def __init__(self, name, rank_my_professor_scores, number_of_startups, number_of_students,
                 avg_undergrad_publications, avg_patent_publications, avg_tuition_paid_usd, open_courses, video_courses,
                 faculty_size, demographic_proportions, national_avg_salary, grad_salary, avg_class_size, yearly_intake, acceptance_rate):
        self.acceptance_rate = acceptance_rate
        self.name = name
        self.rank_my_professor_scores = rank_my_professor_scores
        self.number_of_startups = number_of_startups
        self.number_of_students = number_of_students
        self.avg_undergrad_publications = avg_undergrad_publications
        self.avg_patent_publications = avg_patent_publications
        self.avg_tuition_paid_usd = avg_tuition_paid_usd
        self.open_courses = open_courses
        self.video_courses = video_courses
        self.yearly_intake = yearly_intake
        self.faculty_size = faculty_size
        self.demographic_proportions = demographic_proportions
        self.national_avg_salary = national_avg_salary
        self.grad_salary = grad_salary
        self.avg_class_size = avg_class_size

    def standardized_rank_my_professor_scores(self):
        valid = [d for d in self.rank_my_professor_scores if d > 2]
        if not valid:
            return 0.0
        return (sum(valid) / len(valid)) / 5.0

    def standardized_number_of_startups(self):
        per_1000 = (self.number_of_startups / max(1, self.number_of_students)) * 1000
        return 1 - math.exp(-0.10 * per_1000)

    def score_undergrad_publications(self, ideal=2.5, spread=2.0):
        return math.exp(-((self.avg_undergrad_publications - ideal) ** 2) / (2 * spread ** 2))

    def score_patent_publications(self, ideal=1, spread=2.0):
        return math.exp(-((self.avg_patent_publications - ideal) ** 2) / (2 * spread ** 2))

    def tuition_rating(self):
        return math.exp(-0.000028 * max(0, self.avg_tuition_paid_usd))

    def open_course_size(self):

        weighted_ocw = self.open_courses + (2.0 * self.video_courses)

        per_100_faculty = (weighted_ocw / max(1, self.faculty_size)) * 100

        return 1 - math.exp(-0.05 * per_100_faculty)

    def demographic_proportion_weighting(self):

        general_diversity = len(self.demographic_proportions)
        if general_diversity <= 1:
            return 0.0
        center = 1.0 / general_diversity

        avg_skew = 0
        for i in self.demographic_proportions:
            avg_skew += abs(center - i)

        max_skew = 2.0 * (1.0 - center)

        return (1 - (avg_skew / max_skew)) ** 0.5

    def optimal_acceptance_rate(self):
        sustainable_capacity = max(1, self.faculty_size * 10)
        load_ratio = self.number_of_students / sustainable_capacity

        ideal = 0.40 / load_ratio
        return min(0.55, max(0.20, ideal))

    def score_accessibility(self):
        ideal = self.optimal_acceptance_rate()
        return max(0.0, 1.0 - abs(ideal - self.acceptance_rate) * 1.5)

    def total_score(self):
        scores = [
            self.demographic_proportion_weighting(),
            self.standardized_rank_my_professor_scores(),
            self.standardized_number_of_startups(),
            self.score_undergrad_publications(),
            self.score_patent_publications(),
            self.tuition_rating(),
            self.open_course_size(),
            self.score_class_size(),
            self.score_leaving_salary(),
            self.score_class_size()
        ]
        return round((sum(scores) / len(scores)) * 100, 2)

    def score_leaving_salary(self):

        if self.national_avg_salary <= 0 or self.grad_salary <= 0:
            return 0.0

        ratio = self.grad_salary / self.national_avg_salary
        return 1 - math.exp(-0.8 * ratio)

    def score_class_size(self):

        if self.avg_class_size <= 0:
            return 0.0

        effective_size = max(15.0, float(self.avg_class_size))
        return math.exp(-0.0167 * (effective_size - 15.0))
