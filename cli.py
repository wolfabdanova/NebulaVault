from nebula.wallet import Wallet
from nebula.transaction import Transaction
from nebula.blockchain import Blockchain

def main():
    print("=== NebulaVault CLI ===")

    wallet = Wallet()
    print("Your address:", wallet.get_address())

    blockchain = Blockchain()

    tx = Transaction(wallet.get_address(), "recipient_address", 10)
    blockchain.add_block([tx])

    print("Transaction hash:", tx.calculate_hash())
    print("Blockchain length:", len(blockchain.chain))


if __name__ == "__main__":
    main()
