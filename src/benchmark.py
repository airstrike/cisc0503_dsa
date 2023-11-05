import time
import random
from buffer import BufferArray  # Replace 'your_module_name' with the name of your module

NUM_ARRAYS = 100 #00  # This is the CONSTANT you can change later

def benchmark_remove_methods(name, method1, method2, arrays, remove_element):
    times_method1 = []
    times_method2 = []

    for arr in arrays:
        buffer_array = BufferArray(len(arr))
        for num in arr:
            buffer_array.insert(num)

        start_time = time.time()
        getattr(buffer_array, method1)(remove_element)
        end_time = time.time()
        times_method1.append(end_time - start_time)

        start_time = time.time()
        getattr(buffer_array, method2)(remove_element)
        end_time = time.time()
        times_method2.append(end_time - start_time)

    avg_time_method1 = sum(times_method1) / len(times_method1)
    avg_time_method2 = sum(times_method2) / len(times_method2)

    print(f'\nBenchmarking {name}')
    # print(f'Removing element: {remove_element}')
    print(f"Average time for {method1:<18}: {avg_time_method1:.10f} seconds")
    print(f"Average time for {method2:<18}: {avg_time_method2:.10f} seconds")
    print(f'{"-" * 80}')

arrays_random = [random.sample(range(1, 2**17), 2**i) for i in range(6, 17) for _ in range(NUM_ARRAYS)]
arrays_start_2_6 = [[i for i in range(2**6)] for _ in range(NUM_ARRAYS)]
arrays_end_2_16 = [[i for i in range(2**16)] for _ in range(NUM_ARRAYS)]

# 1. 100% random for 10,000 arrays of varying sizes ranging from 2^6 elements to 2^16 elements
# 2. 10,000 arrays benchmark when the element being removed is at the start of the array for arrays of 2^6 elements
# 3. 10,000 arrays benchmark when the element being removed is at the start of the array for arrays of 2^6 elements
# 4. 10,000 arrays benchmark when the element being removed is at the end of the array for arrays of 2^16 elements
# 5. 10,000 arrays benchmark when the element being removed is at the end of the array for arrays of 2^16 elements
# 6. 10,000 arrays benchmark when the element being removed is at the middle of the array for arrays of 2^16 elements
# 7. 10,000 arrays benchmark when the element being removed is not present in the array

# Fast Remove
# benchmark_remove_methods(f"1. {NUM_ARRAYS} random arrays", "oldRemove", "remove", arrays_random, random.randint(1, 2**17))
# benchmark_remove_methods(f"2. {NUM_ARRAYS} random arrays of length 2^6, first element removed", "oldRemove", "remove", arrays_start_2_6, 0)
# benchmark_remove_methods(f"3. {NUM_ARRAYS} random arrays of length 2^6, last element removed", "oldRemove", "remove", arrays_start_2_6, 0)
# benchmark_remove_methods(f"4. {NUM_ARRAYS} random arrays of length 2^16, first element removed", "oldRemove", "remove", arrays_end_2_16, 2**16 - 1)
# benchmark_remove_methods(f"5. {NUM_ARRAYS} random arrays of length 2^16, last element removed","oldRemove", "remove", arrays_end_2_16, 2**16 - 1)
# benchmark_remove_methods(f"6. {NUM_ARRAYS} random arrays of length 2^16, middle element removed","oldRemove", "remove", arrays_end_2_16, 2**16 // 2)
# benchmark_remove_methods(f"7. {NUM_ARRAYS} random arrays of length 2^16, element not present","oldRemove", "remove", arrays_end_2_16, 2**16 + 1)

# Stable Remove
benchmark_remove_methods(f"1. {NUM_ARRAYS} random arrays", "oldStableRemove", "stableRemove", arrays_random, random.randint(1, 2**17))
benchmark_remove_methods(f"2. {NUM_ARRAYS} random arrays of length 2^6, first element removed", "oldStableRemove", "stableRemove", arrays_start_2_6, 0)
benchmark_remove_methods(f"3. {NUM_ARRAYS} random arrays of length 2^6, last element removed", "oldStableRemove", "stableRemove", arrays_start_2_6, 0)
benchmark_remove_methods(f"4. {NUM_ARRAYS} random arrays of length 2^16, first element removed", "oldStableRemove", "oldRemove", arrays_end_2_16, 2**16 - 1)
benchmark_remove_methods(f"5. {NUM_ARRAYS} random arrays of length 2^16, last element removed","oldStableRemove", "stableRemove", arrays_end_2_16, 2**16 - 1)
benchmark_remove_methods(f"6. {NUM_ARRAYS} random arrays of length 2^16, middle element removed","oldStableRemove", "stableRemove", arrays_end_2_16, 2**16 // 2)
benchmark_remove_methods(f"7. {NUM_ARRAYS} random arrays of length 2^16, element not present","oldStableRemove", "stableRemove", arrays_end_2_16, 2**16 + 1)