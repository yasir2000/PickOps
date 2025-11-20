"""
Smart Contract Deployment (Web3)
Demonstrates: Contract compilation, deployment, interaction with Ethereum
"""

from web3 import Web3
from solcx import compile_source, install_solc
import json
from typing import Dict, Any

# Connect to local Ganache or Hardhat node
WEB3_PROVIDER = "http://localhost:8545"

# Solidity smart contract source
CONTRACT_SOURCE = '''
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 private storedValue;
    address public owner;

    event ValueChanged(uint256 newValue, address changedBy);

    constructor() {
        owner = msg.sender;
        storedValue = 0;
    }

    function set(uint256 value) public {
        storedValue = value;
        emit ValueChanged(value, msg.sender);
    }

    function get() public view returns (uint256) {
        return storedValue;
    }

    function increment() public {
        storedValue += 1;
        emit ValueChanged(storedValue, msg.sender);
    }
}
'''

class SmartContractDeployer:
    """Deploy and interact with smart contracts"""

    def __init__(self, provider_url: str = WEB3_PROVIDER):
        self.w3 = Web3(Web3.HTTPProvider(provider_url))

        if not self.w3.is_connected():
            raise Exception(f"Failed to connect to {provider_url}")

        print(f"✅ Connected to Ethereum node")
        print(f"   Chain ID: {self.w3.eth.chain_id}")
        print(f"   Latest block: {self.w3.eth.block_number}")

        # Set default account (first account from node)
        self.w3.eth.default_account = self.w3.eth.accounts[0]
        print(f"   Using account: {self.w3.eth.default_account}")

    def compile_contract(self, source_code: str) -> Dict[str, Any]:
        """Compile Solidity contract"""

        print("\n🔨 Compiling contract...")

        # Install solidity compiler if needed
        try:
            install_solc('0.8.0')
        except:
            pass  # Already installed

        # Compile
        compiled_sol = compile_source(
            source_code,
            output_values=['abi', 'bin']
        )

        # Get contract interface
        contract_id, contract_interface = compiled_sol.popitem()

        print(f"✅ Contract compiled: {contract_id}")
        return contract_interface

    def deploy_contract(self, contract_interface: Dict[str, Any]) -> tuple:
        """Deploy contract to blockchain"""

        print("\n🚀 Deploying contract...")

        # Create contract object
        Contract = self.w3.eth.contract(
            abi=contract_interface['abi'],
            bytecode=contract_interface['bin']
        )

        # Build deployment transaction
        tx_hash = Contract.constructor().transact()

        # Wait for transaction receipt
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)

        contract_address = tx_receipt.contractAddress

        print(f"✅ Contract deployed!")
        print(f"   Address: {contract_address}")
        print(f"   Gas used: {tx_receipt.gasUsed}")
        print(f"   Block: {tx_receipt.blockNumber}")

        # Return deployed contract instance
        deployed_contract = self.w3.eth.contract(
            address=contract_address,
            abi=contract_interface['abi']
        )

        return deployed_contract, contract_address

    def interact_with_contract(self, contract):
        """Demonstrate contract interactions"""

        print("\n📞 Interacting with contract...")
        print("=" * 60)

        # 1. Read initial value
        print("\n1️⃣  Reading initial value...")
        initial_value = contract.functions.get().call()
        print(f"   Current value: {initial_value}")

        # 2. Set new value
        print("\n2️⃣  Setting value to 42...")
        tx_hash = contract.functions.set(42).transact()
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"   Transaction: {tx_hash.hex()}")
        print(f"   Gas used: {tx_receipt.gasUsed}")

        # 3. Read updated value
        print("\n3️⃣  Reading updated value...")
        new_value = contract.functions.get().call()
        print(f"   Current value: {new_value}")

        # 4. Increment value
        print("\n4️⃣  Incrementing value...")
        tx_hash = contract.functions.increment().transact()
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)

        # 5. Read incremented value
        incremented_value = contract.functions.get().call()
        print(f"   Value after increment: {incremented_value}")

        # 6. Check events
        print("\n5️⃣  Reading events...")
        events = contract.events.ValueChanged.get_logs(fromBlock=tx_receipt.blockNumber)
        for event in events:
            print(f"   Event: Value changed to {event['args']['newValue']} "
                  f"by {event['args']['changedBy']}")

        # 7. Get owner
        print("\n6️⃣  Getting contract owner...")
        owner = contract.functions.owner().call()
        print(f"   Owner: {owner}")

        return {
            'initial_value': initial_value,
            'final_value': incremented_value,
            'owner': owner
        }

def demo_deployment():
    """Complete deployment demo"""

    print("🌐 Smart Contract Deployment Demo")
    print("=" * 60)

    try:
        # Initialize deployer
        deployer = SmartContractDeployer()

        # Compile contract
        contract_interface = deployer.compile_contract(CONTRACT_SOURCE)

        # Deploy contract
        contract, address = deployer.deploy_contract(contract_interface)

        # Interact with contract
        results = deployer.interact_with_contract(contract)

        # Summary
        print("\n" + "=" * 60)
        print("📊 Deployment Summary")
        print("=" * 60)
        print(f"\n✅ Contract deployed at: {address}")
        print(f"   Initial value: {results['initial_value']}")
        print(f"   Final value: {results['final_value']}")
        print(f"   Owner: {results['owner']}")

        # Save deployment info
        deployment_info = {
            'contract_address': address,
            'abi': contract_interface['abi'],
            'owner': results['owner'],
            'network': 'localhost:8545'
        }

        with open('deployment.json', 'w') as f:
            json.dump(deployment_info, f, indent=2)

        print(f"\n💾 Deployment info saved to deployment.json")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\n⚠️  Make sure Ganache or Hardhat node is running:")
        print("   npx hardhat node")
        print("   or")
        print("   ganache-cli")

if __name__ == "__main__":
    # Install: pip install web3 py-solc-x
    # Start local blockchain: npx hardhat node
    demo_deployment()
