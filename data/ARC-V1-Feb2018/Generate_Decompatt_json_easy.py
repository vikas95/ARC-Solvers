import json
from Preprocess_ARC_decompatt import Preprocess_Arc, Preprocess_KB_sentences, Write_ARC_KB, get_IDF_weights, Query_boosting_sent

json_data=open("/Users/vikasy/SEM_5/ARC-Solvers-master/data/ARC-V1-Feb2018/ARC-Easy/ARC-Easy-Test_with_hits_default_or.jsonl","r")
json_data_write=open("/Users/vikasy/SEM_5/ARC-Solvers-master/data/ARC-V1-Feb2018/ARC-Easy/ARC-Easy-Test_with_hits_default.jsonl","w")

cols_sizes, questions, candidates, algebra, All_words, correct_ans, negative_ques, ques_id=Preprocess_Arc("ARC","ARC_corpus/ARC-Challenge/ARC-Challenge-Test.csv").preprocess()

justification_file = open("/Users/vikasy/SEM_5/ARC_EASY/Easy_BIDAF_test_3_60_explanations_BM25.txt","r")
# justification_file = open("/Users/vikasy/SEM_5/ARC_EASY/SIGIR_easy_test_justification.txt","r")

ind2char = {'0':'A', '1':'B', '2':'C', '3':'D', '4':'E'}
char2ind = {'A':'0', 'B':'1', 'C':'2', 'D':'3', 'E':'4'}

Good_justifications = []
Good_justifications_score = []
for line in justification_file:
    all_just1 = line.strip().split("\t")[0:1]
    GJ1 = []
    GJ1_score = []
    for all_just in all_just1:
        good_just1 = " ".join(all_just.split()[1:])
        GJ1.append(good_just1)
        GJ1_score.append(all_just.split()[0])
    Good_justifications.append(GJ1)
    Good_justifications_score.append(GJ1_score)

print(len(Good_justifications))

count =0
for line in json_data:
    count+=1
    if count==1:
       data_dict = json.loads(line)
       break
print(data_dict)

# print(questions[0:2])
# print(correct_ans[0:2], ques_id[0:2])
j_count = 0
for ques_index, question1 in enumerate(questions):
    data_dict['id']=ques_id[ques_index]
    data_dict['answerKey']=ind2char[str(correct_ans[ques_index])]

    data_dict['question']['stem']=question1
    for cind, cand1 in enumerate(candidates[ques_index]):
        data_dict['question']['choice']['text'] = cand1
        # print(ind2char, type(ind2char), cind,  ind2char[str(cind)])
        data_dict['question']['choice']['label'] = ind2char[str(cind)]
        for jind1, just_1 in enumerate(Good_justifications[j_count]):
            data_dict['question']['support']['text'] = just_1
            data_dict['question']['support']['ir_score'] = Good_justifications_score[j_count][jind1]
            data_dict['question']['support']['ir_pos'] = cind
            json.dump(data_dict, json_data_write)
            json_data_write.write('\n')

        j_count+=1

print(j_count)


