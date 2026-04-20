def max_negative_representive(arr) -> int:
    set_for_negatives = set()
    result = -1
    
    for num in arr:
        if num < 0:
            set_for_negatives.add(-num)

    for num in arr:
        if num > 0 and num in set_for_negatives:
            result = max(result, num)
            
    return result


def max_negative_representive_sets(arr):
    # Создаем два множества: положительные и абсолютные значения отрицательных
    positives = {num for num in arr if num > 0}
    negatives = {-num for num in arr if num < 0}

    # Находим общие элементы (пересечение)
    intersection = positives & negatives

    return max(intersection) if intersection else -1
