---
title: "How to Save Gas in your  Ethereum Smart Contracts"
date: 2021-04-08T14:38:02
categories: ["Crypto", "Tuts"]
tags: ["Crypto", "smart contracts"]
image: /assets/uploads/2021/04/save-gas.jpg
---

Gas is a fee mechanism implemented by Ethereum to help with transactions. This fee is a fraction of the transaction presented in Wei, which is 10-12 of an Ether. Total fee price depends on the size of the smart contract and its functionality.

This fee price is dependent on the supply and demand and it is used as a payment for the resources consumed by miners in order to process and validate the transaction to the Ethereum Blockchain. With every operation performed, some cost is added for the transaction. A table of the average cost per transaction can be seen below.

| Operation | Gas | Description |
| --- | --- | --- |
| ADD/SUB | 3 | Arithmetic operation |
| MUL/DIV | 5 | Arithmetic operation |
| ADDMOD/MULMOD | 8 | Arithmetic operation |
| AND/OR/XOR | 3 | Bitwise logic operation |
| LT/GT/SLT/SGT/EQ | 3 | Comparison operation |
| POP | 2 | Stack operation |
| PUSH/DUP/SWAP | 3 | Stack operation |
| MLOAD/MSTORE | 3 | Memory operation |
| JUMP | 8 | Unconditional jump |
| JUMPI | 10 | Conditional jump |
| SLOAD | 200 | Storage operation |
| SSTORE | 5,000/20,000 | Storage operation |
| BALANCE | 400 | Get balance of an account |
| CREATE | 32,000 | Create a new account using CREATE |
| CALL | 25,000 | Create a new account using CALL |

Source: [StackOverflow](https://ethereum.stackexchange.com/a/28848/68347)

### Save on data types

It is better to use uint256 and bytes32 than using uint8 for example. While it seems like uint8 will consume less gas than uint256 it is not true, since the Ethereum virtual Machine(EVM) will still occupy 256 bits, fill 8 bits with the uint variable and fill the extra bites with zeros. In order to verify the following contract was deployed.

```js
pragma solidity ^0.8.1;

contract SaveGas {
    
    uint8 resulta = 0;
    uint resultb = 0;
    
    function UseUint() external returns (uint) {
        uint selectedRange = 50;
        for (uint i=0; i < selectedRange; i++) {
            resultb += 1;
        }
        return resultb;
    }
    
    function UseUInt8() external returns (uint8){
        uint8 selectedRange = 50;
        for (uint8 i=0; i < selectedRange; i++) {
            resulta += 1;
        }
        return resulta;
    }
}
```

So after compiling and deploying the smart contract the functions are available for execution.

[![](/assets/uploads/2021/04/Screenshot-2021-04-08-at-14.39.12.png)](/assets/uploads/2021/04/Screenshot-2021-04-08-at-14.39.12.png)

Firstly executing **UseUint** the following execution cost is presented:

|  |  |
| --- | --- |
| transaction cost | 141654 gas |
| execution cost | **120382 gas** |
|

Next running **UseUint8** the execution cost is:

|  |  |
| --- | --- |
| transaction cost | 187383 gas |
| execution cost | **166111 gas** |

So the execution cost of running uint8 instead of uint256 is higher and the reason is the extra operations for conversions required by the EVM.

### Enable optimiztion

Ethereum’s remix IDE allows to enable optimization, which can increase complexity in a smart contract, but can save on fees. In order to test it the previous badly written contract is complied and deployed again.

[![](/assets/uploads/2021/04/Screenshot-2021-04-08-at-14.59.36.png)](/assets/uploads/2021/04/Screenshot-2021-04-08-at-14.59.36.png)

Now that the new contract is deployed, the same functions are executed and can be seen below:

**UseUint**

|  |  |
| --- | --- |
| transaction cost | 132295 gas |
| execution cost | **111023 gas** |

**UseUint8**

|  |  |
| --- | --- |
| transaction cost | 178253 gas |
| execution cost | **156981 gas** |

The cost for execution was decreased by almost 10%, while using the default optimization of 200. For complicated smart contracts optimization should be increased over 200, so something like 10.000 should be enough, but it was identified that [optimization past 20.000 had no benefits](https://github.com/trusttoken/smart-contracts/pull/76).

### Access data from memory and not from storage

In our example the contract stores 2 variable on its storage, resulta and resultb. While this is ok, both the UseUint and UseUint8 functions loop 50 times over the result variable, accessing it from the storage every single time. Because accessing the memory is cheaper and faster, before going through the loop, the storage variables can be stored in memory. So **reulta** will be **resultaMem** and **resultb** will be **resultbMem**, like shown below.

```js
pragma solidity ^0.8.1;

contract SaveGas {
    
    uint8 resulta = 0;
    uint resultb = 0;
    
    function UseUint() external returns (uint) {
        uint selectedRange = 50;
        uint resultbMem = resultb;
        for (uint i=0; i < selectedRange; i++) {
            resultbMem += 1;
        }
        return resultbMem;
    }
    
    function UseUInt8() external returns (uint8){
        uint8 selectedRange = 50;
        uint8 resultaMem = resulta;
        for (uint8 i=0; i < selectedRange; i++) {
            resultaMem += 1;
        }
        return resultaMem;
    }
}
```

[![](/assets/uploads/2021/04/Screenshot-2021-04-08-at-15.17.12.png)](/assets/uploads/2021/04/Screenshot-2021-04-08-at-15.17.12.png)

Now one again, compile and deploy the smart contract to observe how the cost has change.

**UseUint**

|  |  |
| --- | --- |
| transaction cost | 31951 gas |
| execution cost | **10679 gas** |

**UseUint8**

|  |  |
| --- | --- |
| transaction cost | 34506 gas |
| execution cost | **13234 gas** |

With a small edit, the cost of this contract is decreased by a tenfold, which is great. From 111k gas it went to 10k gas for Uint and for Uint8 it went from 160k gas to 13k gas.

### Further Reading

There are more and more thing you should take into consideration before deploying your mart contract in production.

- [8 Ways of Reducing the Gas Consumption of your Smart Contracts](https://medium.com/coinmonks/8-ways-of-reducing-the-gas-consumption-of-your-smart-contracts-9a506b339c0a)
- [How to Write Smart Contracts That Optimize Gas Spent on Ethereum](https://betterprogramming.pub/how-to-write-smart-contracts-that-optimize-gas-spent-on-ethereum-30b5e9c5db85)
- [How to write an optimized (gas-cost) smart contract?](https://ethereum.stackexchange.com/questions/28813/how-to-write-an-optimized-gas-cost-smart-contract)
