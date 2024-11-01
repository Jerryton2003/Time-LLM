model_name=TimeLLM
train_epochs=100
learning_rate=0.01
llama_layers=32

master_port=00097
num_process=2
batch_size=16
d_model=32
d_ff=128

comment='TimeLLM_AS'

accelerate launch --multi_gpu --mixed_precision bf16 --num_processes $num_process --main_process_port $master_port run_main.py \
  --task_name long_term_forecast \
  --is_training 1 \
  --root_path ./dataset/ \
  --data_path  P_DKASC.csv\
  --model_id DKASC_512_96 \
  --model $model_name \
  --data AS \
  --features S \
  --target 'hourly_data' \
  --seq_len 512 \
  --label_len 48 \
  --pred_len 96 \
  --factor 3 \
  --enc_in 7 \
  --dec_in 7 \
  --c_out 7 \
  --des 'Exp' \
  --itr 1 \
  --d_model $d_model \
  --d_ff $d_ff \
  --batch_size $batch_size \
  --learning_rate $learning_rate \
  --llm_layers $llama_layers \
  --train_epochs $train_epochs \
  --model_comment $comment