tries = 5
eps = 0.001
total_marks = 10
failed_cases = []
def test_run_syncode():
    correct = 0
    for i in range(len(cases)):
        full_correct = False
        for t in range(tries):
            try:
                model_answer = run_syncode(cases[i])
            except:
                print(f'student error on {i+1}')
                continue
            print(f"student answer on {i+1}:", model_answer)
            if i == 0 and t == 0:
              input("ok?")
            gt_answer = answers[i]
            this_correct = True
            if abs(model_answer[0][0]-gt_answer[0][0]) > eps:
                this_correct = False
            if abs(model_answer[0][1] - gt_answer[0][1]) > eps:
                this_correct = False 
            if model_answer[1] != gt_answer[1]:
                this_correct = False 
            if abs(model_answer[2] - gt_answer[2]) > eps:
                this_correct = False
            if this_correct:
                full_correct = True
                break
        if not full_correct:
            failed_cases.append(str(i+1))
        correct += full_correct
    print("correct:", correct, "total:", len(cases))
    print("Failed on test cases:",', '.join(failed_cases))
    print("Marks deducted:", ((len(cases)-correct)/len(cases))*total_marks)

test_run_syncode()