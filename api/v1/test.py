#!/usr/bin/env python3
"""
Test
"""
import numpy as np
from xtoxica import Toxicity_model

toxicities = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]

XToxica = Toxicity_model()
comment = "I Love your Work"

pred = XToxica.xtoxica(comment)
print(pred, type(pred))
