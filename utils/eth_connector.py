from web3 import Web3
import web3


class EthNode:
    account = None
    eth_node = None
    local = False

    def __init__(self, rpc_url, private_key):
        self.eth_node = Web3(Web3.HTTPProvider(rpc_url))
        if rpc_url == 'http://127.0.0.1:8545':
            w3 = web3.Web3(web3.HTTPProvider(rpc_url))
            # w3.eth.accounts()[0]
            self.local = True
            self.account = '0xf4F8040E3D9505f7d9F661Ca174435B41e39304D'
        else:
            self.account = self.eth_node.eth.account.privateKeyToAccount(
                private_key)

    def make_tx(self, tx):
        print(self.account.address)
        self.eth_node.eth.call(tx)
        tx['nonce'] = self.eth_node.eth.get_transaction_count(
            self.account.address)
        tx['gas'] = 8000000
        # tx['chainId'] = self.eth_node.eth.chain_id
        if self.local:
            tx.pop('maxPriorityFeePerGas')
            tx.pop('maxFeePerGas')
        tx['gasPrice'] = self.eth_node.toWei('2', 'gwei')
        signed_tx = self.eth_node.eth.account.sign_transaction(
            tx, self.account.key)
        tx_hash = self.eth_node.eth.send_raw_transaction(
            signed_tx.rawTransaction)
        tx_receipt = self.eth_node.eth.wait_for_transaction_receipt(tx_hash)
        print(tx_receipt)
        if tx_receipt.status == 1:
            print('TX successful')
        else:
            print('TX reverted')

    def get_balance(self, address):
        return self.eth_node.eth.get_balance(address) / 10 ** 18
