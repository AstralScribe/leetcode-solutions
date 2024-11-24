from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid_list = []

        valid_dict = {}

        def get_transaction(transaction: str) -> List:
            chars = []
            output = []
            for t in transaction:
                if t == ",":
                    output.append("".join(chars))
                    chars = []
                    continue
                chars.append(t)
            output.append("".join(chars))

            output[1] = int(output[1])
            output[2] = int(output[2])

            return output

        for transaction in transactions:
            transaction_details = get_transaction(transaction)

            if transaction_details[2] > 1000:
                invalid_list.append(transaction)
                continue

            existing_name = valid_dict.get(transaction_details[0], {})

            if not existing_name:
                valid_dict[transaction_details[0]] = {transaction: transaction_details}
                continue
            else:
                for t, td in existing_name.items():
                    temp = {t: td}
                    if (
                        abs(transaction_details[1] - td[1]) <= 60
                        and transaction_details[3] != td[3]
                    ):
                        if invalid_list.count(t) == 0:
                            invalid_list.append(t)
                        if invalid_list.count(transaction) == 0:
                            invalid_list.append(transaction)
                    else:
                        temp[transaction] = transaction_details
                valid_dict[transaction_details[0]] = temp

        return invalid_list


s = Solution()

case = ["alice,20,800,mtv", "alice,50,100,mtv", "alice,51,100,frankfurt"]

print(s.invalidTransactions(case))
