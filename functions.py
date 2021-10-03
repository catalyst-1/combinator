def combine(array , pointer):
#pointer points where to get value
        if pointer == 0:
                return array
        return combine(array,pointer-1) + array[pointer-1]
def magic(str):
        for ai in str:
                for bi in str:
                        print(ai+bi)
        return 0
