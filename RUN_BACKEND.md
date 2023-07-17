# Backend

This backend allows for easily managing of the staking pool.

It can:

- Create Validator keys (for Deposit)
- Generate Keyshares (for SSV contract)
- Deposit Keyshares
- Deposit Validators
- monitor staking pool balance, create + deposit the validator to beacon chain and create + deposit keyshares to ssv network.

## Prerequiste - Smart contract deployments

You need to have smart contracts deployed before running this backend. After deployed, continue with this tutorial. You can choose to deploy them together with frontend using scaffold-eth framework built in `JS` or deploy smart contracts only with brownie framework built in `PY`.

### 1. Front End plus Smart contracts - Scaffold-eth framework

Continue to README in `frontend` folder [FE_README.md](/frontend/README.md)

It will navigate you through the remaining process. Come back once smart contracts are deployed.

If you want to deploy smart contracts only using brownie framework continue to the next step.

### 2. Smart Contracts Only - Brownie framework

Continue to README [RUN_SMART_CONTRACTS_ONLY.md](/RUN_SMART_CONTRACTS_ONLY.md) to deploy smart contract only using brownie framework.

It will navigate you through the remaining process. Come back once smart contracts are deployed.

### External Libraries used

- [SSV-KEYS](https://github.com/bloxapp/ssv-keys.git) : Used to split Ethereum validator keys.

- [Ethereum-staking-cli](https://github.com/ethereum/staking-deposit-cli.git) : Used to generate Ethereum validators keys

## Install Dependencies

- [python](https://www.python.org/downloads/), you can install it here.

## Initial setup

- make the script executable and run it

```

chmod +x setup.sh

./setup.sh


```

## Run Backend Manager

**IMPORTANT:**

- **Backend Manager is whitelisted**
  - Make sure that for the backend script, you are using a private key corresponding to your `whitelist` address from your `deploy` script.

- **Backend Manager has SSV balance**
  - Your staking pool needs to be funded with some SSV to pay for running your validator. Keep at least 50 SSV at your deployer address. It will be used to pay operators for running your distributed validator. You can get some Goerli SSV from [SSV faucet here](https://faucet.ssv.network/). If you are using a local goerli-fork, use the faucet on Goerli, send the SSV to your deployer address and launch your goerli-fork again.

### Outputs

Your created validator keys and deposit data can be found in `"/validator_keys"` folder.

Validator split shares can be found in `"/keyshares"` folder.

#### How to use it

- _stake_ : This is the backend script that monitors the staking pool and generates validator keys, SSV keyshares and send transactions to submit them.

  - Example config file: sample_config/stake-config.json
  - Fill in the params in the config file and pass it as an argument

**NOTE:**

- For `"rpc:"` value use `http://localhost:8545` if you are connecting to goerli-fork and `https://goerli.infura.io/v3/<your id>` when connecting to goerli.
- For `"goerli_rpc:"` **alwyas** use goerli rpc endpoint `https://goerli.infura.io/v3/<your id>`, no matter if you are connecting to goerli-fork or live goerli. This is necessary for correctly fetching clusters.

```
python3 main.py stake -c <CONFIG_FILE>


python3 main.py stake -c sample_config/stake-config.json

```

validator_keys

- Open a new terminal in the main project folder

To run the scripts you first need to install the requirements :

```

pip install -r requirements.txt

```

To see what command line options the script supports :

```

python3 main.py -h/--help

```

Following are the option and their respective config:

- _create-keys_ : This option can be used to generate Ethereum validator keys and their deposit data
  - Example config file: sample_config/validator-config.json
  - Fill in the params in the config file and pass it as an argument

```

python3 main.py create-keys -c <CONFIG_FILE>

e.g.

python3 main.py create-keys -c sample_config/validator-config.json

```

- _generate-keyshares_ : This option can be used to generate SSV keyshares using the SSV CLI tool
  - Example config file: sample_config/keyshare-config.json
  - Fill in the params in the config file and pass it as an argument

```

python3 main.py generate-keyshares -c <CONFIG_FILE>

e.g.

python3 main.py generate-keyshares -c sample_config/keyshare-config.json

```

- _deposit-validators_ : This option can be used to submit validator keys to the staking pool
  - Example config file: sample_config/deposit-validator.json
  - Fill in the params in the config file and pass it as an argument

```

python3 main.py deposit-validators -c <CONFIG_FILE>

e.g.

python3 main.py deposit-validators -c sample_config/deposit-validator.json

```

- _deposit-keyshares_ : This option can be used to submit validator keyshares to the staking pool
  - Example config file: sample_config/deposit-keyshares.json
  - Fill in the params in the config file and pass it as an argument

```

python3 main.py deposit-keyshares -c <CONFIG_FILE>

```
- *exit* : This option can be used to exit the validator keys on testnet with keystore file and password
  - Example config file: sample_config/exit_config.json
  - Fill in the params in the config and pass it as an argument
```
python main.py exit -c <CONFIG_FILE>
```

### LICENSE

MIT License
