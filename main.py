from helpers.csv import read_csv

universities = read_csv("data/universities.csv")

ranked = sorted(universities, key=lambda u: u.total_score(), reverse=True)

print(
    f"{'Rank':<4} | {'University':<28} | {'Total Score':>11} | {'Optimal Acc%':>12} | {'Actual Acc%':>11} |"
    f" {'Accessibility':>13} | {'Startups':>8} | {'Patents':>7} | {'Tuition':>7} | {'Salary':>6} | {'Class Size':>10}"
)
print("-" * 149)
for idx, u in enumerate(ranked, start=1):
    print(
        f"#{idx:<3} | {u.name:<28} | {u.total_score():>11.2f} | "
        f"{u.optimal_acceptance_rate()*100:>11.0f}% | "
        f"{u.acceptance_rate*100:>10.0f}% | "
        f"{u.score_accessibility():>13.2f} | "
        f"{u.standardized_number_of_startups():>8.2f} | "
        f"{u.score_patent_publications():>7.2f} | "
        f"{u.tuition_rating():>7.2f} | "
        f"{u.score_leaving_salary():>6.2f} | "
        f"{u.score_class_size():>10.2f}"
    )