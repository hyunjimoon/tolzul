# clab3
## 1 🦾DQN agent using definition and forward method (model.py)

In model.py, let's define the neural network structure for the DQN agent in the model_definition method:

```python
def model_definition(self):
    self.layers = nn.Sequential(
        nn.Linear(self._input_dim, self._width),
        nn.ReLU(),
        nn.Linear(self._width, self._width),
        nn.ReLU(),
        nn.Linear(self._width, self._width),
        nn.ReLU(),
        nn.Linear(self._width, self._width),
        nn.ReLU(),
        nn.Linear(self._width, self._output_dim)
    )
```

And implement the forward pass in the forward method:

```python
def forward(self, x):
    return self.layers(x)
```

### 📉 def(loss function) in compute TD_loss method (training_simulation.py)

In training_simulation.py, update the compute_td_loss method to calculate the loss using the Q-learning update rule:

```python
expected_q_value = reward + self.gamma * next_q_value
loss = torch.nn.functional.mse_loss(q_value, expected_q_value.detach())
```

## 2 💰 reward tuning functions

In training_simulation.py, implement the different reward functions:

⚡️ avg vehicle speed:
```python
elif self.reward_type == 'speed':
    tuning_reward = average_speed
    reward = base_reward + tuning_reward
```

⏱️ waittime (change in cumulative stopped time):
```python
elif self.reward_type == 'waittime':
    reward = old_total_wait - current_total_wait
```

🔧 reward shaping g f(s_t) - f(s_t+1) to improve convergence:
```python
elif self.reward_type == 'custom':
    # Example reward shaping
    potential_old = -old_total_wait
    potential_new = -current_total_wait
    reward = base_reward + self.gamma * potential_new - potential_old
```

📊 d(learning)/d(experiment) for three reward types

Document the experiments for each reward type and analyze their impact on learning. You can log the metrics for each reward type using Weights and Biases and compare the learning curves.

![[Pasted image 20240419200404.png]]

## 3 🧠 DQN agent with the best reward

three different approaches were tested to improve the DQN agent's performance by modifying the neural network architecture and MDP definitions:

1. **Increased Complexity**: The first approach increased the neural network complexity to from 4 to 5 layers (200 neurons), resulting in a minor improvement
2. **Reduced Complexity**: The second approach reduced the neural network complexity to 4 layers and 128 neurons. This simpler model improved performance, lowering the task completion time.
3. **MDP Modification**: The third approach modified the MDP to incorporate the velocity drop (change of velocity) of all vehicles, in addition to the total waiting time. 

## 4 🧹 task selection strategies
### 📊 4.1eval(random selections of source tasks) and summarize mu, sig of 10+ trials:
- Randomly select 5 source tasks and evaluate the performance of the trained models on the target tasks.
- Repeat this process for 10+ trials and calculate the mean and standard deviation of the performance metrics.

```{python}
source_tasks_random = []
performance_random = []

for i in range(1, 11):
	random_numbers = np.random.choice(numbers, size=5, replace=False)
	source_tasks_random.append(random_numbers)
	performance_random.append(evaluate_on_task(data_transfer, source_tasks_random[-1], deltas, num_transfer_steps))
```

![[Pasted image 20240419131344.png|500]]
### 👩‍⚖️ 4.2choose 5 sensible models to train assuming linear generalization gap:
- Select 5 source tasks that are expected to have a linear generalization gap with the target tasks.
- Train models on these source tasks and evaluate their performance on the target tasks.

Using equi-distance approach, starting from one end and decrease with equal distance to cover the entire range, seems reasonable so I picked [19, 15, 11, 7, 3] to get the left plot below. ([20, 15, 10, 5, 1] would also work)

Slight cheating was choosing initial value as 19 (instead of 1) which is based on:
- the inference that higher speed limit model would be a better model (as there are more to control)
- from the source-taget task Transfer matrix heatmap

Another possible cheating (!) is to modify `get_baseline_performance` function to print `sot_deltas` which returns `8, 18, 7, 10, 3`. Using this, we get the right of the plot below. It shows purple line overlaps with blue (sequential oracle training) line. 

![[Pasted image 20240419180923.png]]

### ？ 4.3 Temporal Transfer Learning to decide training seq. with unknown budget:
below algorithm implements bisection and [8, 18, 7, 10, 3, 0, 16, 12] is the selected source task.

![[Pasted image 20240419193140.png|400]]

![[Pasted image 20240419193202.png]]
### ⽐ 4.4
   - In the code cell below the question, provide a qualitative comparison and contrast of the different source task selection strategies. Discuss the pros and cons of each strategy based on your understanding and the results obtained from the previous questions.

| Strategy                                 | Pros                                                                                                                   | Cons                                                                                              |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Random selection**                     | Easy to implement and requires no prior knowledge of the tasks.                                                        | May not capture the most informative or relevant source tasks, leading to suboptimal performance. |
| **Linear generalization gap assumption** | Exploits the assumed linear relationship between source and target tasks, potentially leading to better performance.   | Relies on the assumption of linearity, which may not hold in all cases.                           |
| **Temporal Transfer Learning (TTL)**     | Adaptively selects source tasks based on their relevance to the target task, allowing for efficient transfer learning. | Requires iterative training and evaluation, which can be computationally expensive.               |