# pylotus
Python Wrapper for Filecoin Lotus API

# Example

You will need API key from lotus-miner

    pip3 install git+https://github.com/Tualua/pylotus.git
    python3
    >>> from pylotus import LotusMiner
    >>> LM = LotusMiner('http://127.0.0.1:2345/rpc/v0', 'e...Q')
    >>> print(LM.get_sectors_summary())
    {'Proving': 5, 'Removing': 1, 'WaitSeed': 1}

Methods available:

- Filecoin.SectorsList
- Filecoin.SectorsSummary
- Filecoin.WorkerStats (need admin key)
- Filecoin.WorkerJobs (need admin key)
