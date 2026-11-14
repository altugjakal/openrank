import csv

from university import University


def read_csv(filename):
    universities = []
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rmp_scores = [
                float(x)
                for x in row["rank_my_professor_scores"].split("|")
                if x.strip()
            ]
            demographics = [
                float(x)
                for x in row["demographic_proportions"].split("|")
                if x.strip()
            ]

            uni = University(
                name=row["name"].strip(),
                rank_my_professor_scores=rmp_scores,
                number_of_startups=int(row["number_of_startups"]),
                number_of_students=int(row["number_of_students"]),
                avg_undergrad_publications=float(row["avg_undergrad_publications"]),
                avg_patent_publications=float(row["avg_patent_publications"]),
                avg_tuition_paid_usd=float(row["avg_tuition_paid_usd"]),
                open_courses=int(row["open_courses"]),
                video_courses=int(row["video_courses"]),
                faculty_size=int(row["faculty_size"]),
                demographic_proportions=demographics,
                national_avg_salary=float(row["national_avg_salary"]),
                grad_salary=float(row["grad_salary"]),
                avg_class_size=float(row["avg_class_size"]),
                yearly_intake=int(row["yearly_intake"]),
                acceptance_rate=float(row["acceptance_rate"]),
            )
            universities.append(uni)
        return universities