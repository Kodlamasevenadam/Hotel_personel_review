
# Çalışanların puanını hesaplayan modül.


from worker_points import *

import os
while True:
    try:
        import worker_infos
        break
    except ImportError:
        print("worker_infos.py not found. Please ensure it is in the same directory as this script.")
        break
print("Welcome to the Hotel Worker Evaluation System")
print("Available workers:")
for worker in Worker_list:
    print(f"- {worker.name}, Age: {worker.age}, Position: {worker.position}, Points: {worker.points}")
print("\nYou can evaluate a worker by entering their name.")

worker_name = input("Enter the name of the worker you want to evaluate: ")


def find_worker_by_name(name, workers):
    for worker in workers:
        if worker.name.lower() == name.lower():
            return worker
    return None


worker = find_worker_by_name(worker_name, Worker_list)
if worker:
    print(
        f"Worker found: {worker.name}, Age: {worker.age}, Position: {worker.position}, Points: {worker.points}")
    input_points = input("Enter the points to evaluate the worker: ")
    try:
        points = float(input_points)

        if points < 0 or points > 100:
            print("Points must be between 0 and 100.")

        else:
            worker.points = (worker.points + points) / 2
            print(f"Points for {worker.name} updated to {worker.points}.")

    except ValueError:
        print("Invalid input. Please enter a number between 0 and 100.")

else:
    print("Worker not found.")
print("Thank you for using the Hotel Worker Evaluation System!")
