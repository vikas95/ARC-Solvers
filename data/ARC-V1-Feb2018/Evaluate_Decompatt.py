import json

# json_data=open("ARC-Challenge/ARC-Challenge-Test_predictions_decompatt_default.jsonl","r")
json_data=open("ARC-Easy/ARC-Easy-Test_predictions_decompatt_default.jsonl","r")


count =0
tot_len = 0

accuracy = 0

cand_score = []
cand_label = []

for line in json_data:


    data_dict = json.loads(line)
    if count==0:
       prev_ques_id = data_dict["id"]
       correct_label = data_dict['answerKey']
    count += 1
    ques_id = data_dict["id"]
    if ques_id == prev_ques_id:
       correct_label = data_dict['answerKey']
       cand_score.append(data_dict['score'])
       cand_label.append(data_dict['question']['choice']['label'])
    else:
       tot_len+=1
       pred_label = cand_label[cand_score.index(max(cand_score))]
       if pred_label==correct_label:
          accuracy+=1

       cand_label=[]
       cand_score=[]

       correct_label = data_dict['answerKey']
       cand_score.append(data_dict['score'])
       cand_label.append(data_dict['question']['choice']['label'])
       prev_ques_id = data_dict['id']


print("total len is: ", tot_len, accuracy)

