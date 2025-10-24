import pytest
import functions

def test_add_positive():
    assert functions.add(25,50) == 75
def test_add_negative():
    assert functions.add(-36, -4) == -40
def test_add_both():
    assert functions.add(-42, 55) == 13

def test_sub_positive():
    assert functions.sub(36,12) == 24
def test_sub_negative():
    assert functions.sub(-12,-8) == -4
def test_sub_negative_result():
    assert functions.sub(20, 42)

def test_mul_positive():
    assert functions.mul(5,10) == 50
def test_mul_negative():
    assert functions.mul(-4, 4) == -16
def test_mul_zero():
    assert functions.mul(8,0) == 0

def test_div_positive():
    assert functions.div(50,5) == 10
def test_div_negative():
    assert functions.div(36, -6) == -6
def test_div_uno():
    assert functions.div(42,1) == 42
def test_div_zero():
    assert functions.div(1337,0) == 'divide_by_zero_error'

def test_exp_positive():
    assert functions.exp(5,2) == 25
def test_exp_negative():
    assert functions.exp(25,-2) == 5
def test_exp_negative():
    assert functions.exp(-5,2) == 'imaginary_result_error'


