score_table = {
    "IBT": [120, 120, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72],
    "ITP": [677, 673, 670, 667, 663, 657, 653, 650, 647, 643, 640, 637, 633, 630, 627, 623, 620, 617, 613, 610, 607, 603, 600, 597, 593, 590, 587, None, 583, 580, 577, None, 573, 570, 567, None, 563, 563, 560, 557, 553, 550, None, 547, None, 543, None, 540, 537, 533, None],
    "IELTS": [9, None, None, None, None, None, None, None, None, 8, None, None, None, None, 7.5, None, None, None, None, None, None, None, 7, None, None, None, None, None, None, 6.5, None, None, None, None, None, None, None, None, None, None, 6, None, None, None, None, None, None, None, None]
}

def get_ibt_equivalent(itp=None, ielts=None):
    """
    Convert ITP or IELTS scores to IBT equivalent.
    """
    if itp:
        try:
            index = score_table["ITP"].index(itp)
            return score_table["IBT"][index]
        except ValueError:
            raise ValueError(f"ITP score {itp} does not have a corresponding IBT score.")
    if ielts:
        try:
            index = score_table["IELTS"].index(ielts)
            return score_table["IBT"][index]
        except ValueError:
            raise ValueError(f"IELTS score {ielts} does not have a corresponding IBT score.")
    return None

def calculate_language_score(ibt=None, itp=None, ielts=None):
    """
    Calculate the language score by converting ITP or IELTS to IBT and using IBT to compute.
    """
    if itp:
        ibt = get_ibt_equivalent(itp=itp)
    elif ielts:
        ibt = get_ibt_equivalent(ielts=ielts)

    if ibt:
        return round(((ibt - 72) / (120 - 72)) * 40, 3)
    return 0

def calculate_final_score(grade=3.0, ibt=None, itp=None, ielts=None, doc_score=10, bonus=0):
    """
    Calculate the final score for exchange student evaluation.
    """
    # Ensure grade meets minimum requirement
    if grade < 3.0:
        return "최저 학점 점수 미충족"

    # Convert ITP and IELTS to IBT if available
    converted_ibt_scores = []
    if ibt and ibt >= 72:
        converted_ibt_scores.append(ibt)
    if itp and itp >= 543:
        try:
            converted_ibt_scores.append(get_ibt_equivalent(itp=itp))
        except ValueError:
            pass
    if ielts and ielts >= 6.0:
        try:
            converted_ibt_scores.append(get_ibt_equivalent(ielts=ielts))
        except ValueError:
            pass

    # Check if any language score meets the criteria
    if not converted_ibt_scores:
        return "최저 어학 점수 미충족"

    # Use the highest IBT score to calculate the language score
    max_ibt = max(converted_ibt_scores)
    language_score = round((max_ibt * 40 / 120), 3)

    # Calculate grade score
    grade_score = round((grade / 4.3) * 50, 3)

    # Calculate final score
    final_score = grade_score + language_score + doc_score + bonus
    return round(final_score, 3)

# Debugging example
if __name__ == "__main__":
    print(calculate_final_score(grade=3.8, itp=580, bonus=5))
    print(calculate_final_score(grade=3.5, ibt=85))
    print(calculate_final_score(grade=2.9, itp=600))  # Should fail due to grade
    print(calculate_final_score(grade=3.6, ielts=6.5, bonus=2))
