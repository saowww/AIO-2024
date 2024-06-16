import random
import math


def random_number(min, max):
    return random.uniform(min, max)


def excercise3():
    try:
        num_samples = input("Input number of samples: ")
        if not num_samples.isnumeric():
            raise Exception("num_samples must be a number")
        loss_name = input("Input loss function (mae|mse|rmse): ")
        num_samples = int(num_sammples)
        match loss_name:
            case "mae":
                final = calculate_mae(num_samples)
            case "mse":
                final = calculate_mse(num_samples)
            case "rmse":
                final = calculate_rmse(num_samples)
            case _:
                raise Exception(f"{loss_name} is not supported")
        print(f"final: {loss_name.upper()}: {final}")

    except Exception as e:
        print(e)


def calculate_mae(num_samples):
    sum_loss = 0
    for sample in range(num_samples):
        target = random_number(1, 10)
        predict = random_number(1, 10)
        loss = abs(target - predict)
        sum_loss += loss
        print(
            f"loss name: MAE, sample: {sample}, pred: {predict}, target: {target}, loss: {loss}")

    return sum_loss/num_samples


def calculate_mse(num_samples):
    sum_loss = 0
    for sample in range(num_samples):
        target = random_number(1, 10)
        predict = random_number(1, 10)
        loss = (target - predict)**2
        sum_loss += loss

        print(
            f"loss name: MSE, sample: {sample}, pred: {predict}, target: {target}, loss: {loss}")

        return sum_loss / num_samples


def calculate_rmse(num_samples):
    sum_loss = 0
    for sample in range(num_samples):
        target = random_number(1, 10)
        predict = random_number(1, 10)
        loss = (target - predict) ** 2
        sum_loss += loss

        print(
            f"loss name: RMSE, sample: {sample}, pred: {predict}, target: {target}, loss: {loss}")

    return math.sqrt(sum_loss/num_samples)


excercise3()
