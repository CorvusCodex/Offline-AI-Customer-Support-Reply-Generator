from utils import run_llama

def support_reply(complaint):
    prompt = f"Write a polite and professional customer support reply to this complaint:\n{complaint}"
    return run_llama(prompt)

if __name__ == "__main__":
    complaint = input("Customer complaint: ")
    print(support_reply(complaint))
