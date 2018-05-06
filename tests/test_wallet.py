# -*- coding: utf-8 -*-
import sys

sys.path.append('../')

import pytest
import os
import datetime

import pyqiwi
from pyqiwi import Wallet

should_skip = 'TOKEN' and 'NUMBER' not in os.environ

if not should_skip:
    TOKEN = os.environ['TOKEN']
    NUMBER = os.environ['NUMBER']


@pytest.mark.skipif(should_skip, reason="No environment variables configured")
class TestWallet:
    def test_create_wallet(self):
        qiwi_wallet = Wallet(TOKEN, number=NUMBER)
        assert isinstance(qiwi_wallet, Wallet)

    def test_check_balance(self):
        qiwi_wallet = Wallet(TOKEN, number=NUMBER)
        assert isinstance(qiwi_wallet, Wallet)
        assert type(qiwi_wallet.balance()) == float

    def test_check_history(self):
        qiwi_wallet = Wallet(TOKEN, number=NUMBER)
        assert isinstance(qiwi_wallet, Wallet)
        history = qiwi_wallet.history()
        assert type(history) == dict
        for tnx in history['transactions']:
            assert type(tnx) == pyqiwi.types.Transaction
        assert type(history['next_txn_date']) == datetime.datetime
        assert type(history['next_txn_id']) == int

    def test_check_profile(self):
        qiwi_wallet = Wallet(TOKEN, number=NUMBER)
        assert isinstance(qiwi_wallet, Wallet)
        profile = qiwi_wallet.profile
        assert type(profile) == pyqiwi.types.Profile

    def test_stat(self):
        qiwi_wallet = Wallet(TOKEN, number=NUMBER)
        assert isinstance(qiwi_wallet, Wallet)
        stat = qiwi_wallet.stat()
        assert type(stat) == pyqiwi.types.Statistics

    def test_check_accounts(self):
        qiwi_wallet = Wallet(TOKEN, number=NUMBER)
        assert isinstance(qiwi_wallet, Wallet)
        accounts = qiwi_wallet.offered_accounts
        for account in accounts:
            assert type(account) == pyqiwi.types.Account