#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

FLEMISH_INDEX = inquisition.SPANISH.index('Spanish')

FLEMISH_LEN = len('Spanish')

FLEMISH_SLICE1 = inquisition.SPANISH[:19]

FLEMISH_SLICE2 = inquisition.SPANISH[19:26]

FLEMISH_SLICE3 = inquisition.SPANISH[26:]

FLEMISH = FLEMISH_SLICE1 + 'Flemish' + FLEMISH_SLICE3
