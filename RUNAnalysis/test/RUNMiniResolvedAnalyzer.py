#!/usr/bin/env python

'''
File: MyAnalyzer.py --mass 50 (optional) --debug -- final --jetAlgo AK5
Author: Alejandro Gomez Espinosa
Email: gomez@physics.rutgers.edu
Description: My Analyzer 
'''

import sys,os,time
#import optparse
import argparse
#from collections import defaultdict
<<<<<<< HEAD
from multiprocessing import Process
=======
>>>>>>> 1ed1f13e9a39e2d9412a067d05462ef0c0cedbeb
from ROOT import TFile, TTree, TDirectory, gDirectory, gROOT, TH1F, TH2D, TMath, TLorentzVector, TVector3
from array import array
from scaleFactors import scaleFactor as SF

gROOT.SetBatch()

def Pairing( tmpj1, tmpj2, tmpj3, tmpj4, offset ):
	"""docstring for Pairing"""

	deltaRPairing = {}
	Pairing = False
	j1 = TLorentzVector()
	j2 = TLorentzVector()
	j3 = TLorentzVector()
	j4 = TLorentzVector()
	deltaRPairing[ '1234' ] = ( abs( tmpj1.DeltaR(tmpj2) - offset ) + abs( tmpj3.DeltaR(tmpj4) - offset ) )
	deltaRPairing[ '1324' ] = ( abs( tmpj1.DeltaR(tmpj3) - offset ) + abs( tmpj2.DeltaR(tmpj4) - offset ) )
	deltaRPairing[ '1423' ] = ( abs( tmpj1.DeltaR(tmpj4) - offset ) + abs( tmpj2.DeltaR(tmpj3) - offset ) )

	minDeltaRPairing = min(deltaRPairing, key=deltaRPairing.get)

	if( '1234' in minDeltaRPairing ):
		j1 = tmpj1
		j2 = tmpj2
		j3 = tmpj3
		j4 = tmpj4
		Pairing = True
	elif( '1324' in minDeltaRPairing ):
		j1 = tmpj1
		j2 = tmpj3
		j3 = tmpj2
		j4 = tmpj4
		Pairing = True
	elif( '1423' in minDeltaRPairing ):
		j1 = tmpj1
		j2 = tmpj4
		j3 = tmpj2
		j4 = tmpj3
		Pairing = True

	return [ Pairing, j1, j2, j3, j4, deltaRPairing[ minDeltaRPairing ] ]


######################################
def myAnalyzer( sample, couts ):


	inputFile = TFile( sample, 'read' )
	outputFileName = sample.replace('RUNAnalysis','RUNMiniResolvedAnalysis')
	outputFile = TFile( outputFileName, 'RECREATE' )
	#outputFile = TFile( 'test.root', 'RECREATE' )

	###################################### output Tree
	#AvgMass = array( 'f', [ 0. ] )
	#tree.Branch( 'AvgMass', AvgMass, 'AvgMass/F' )
	#Scale = array( 'f', [ 0. ] )
	#tree.Branch( 'Scale', Scale, 'Scale/F' )


	################################################################################################## Trigger Histos
	nBinsMass	= 100
	maxMass		= 1000
	nBinsHT		= 150
	maxHT		= 1500

<<<<<<< HEAD
	deltaR_Pairing03 	= TH1F('deltaR_Pairing03', 'deltaR_Pairing03', 100, 0, 5. )
	massAve_Pairing03 	= TH1F('massAve_Pairing03', 'massAve_Pairing03', nBinsMass, 0, maxMass )
	deltaR_Pairing03_Pt50 	= TH1F('deltaR_Pairing03_Pt50', 'deltaR_Pairing03_Pt50', 100, 0, 5. )
	massAve_Pairing03_Pt50 	= TH1F('massAve_Pairing03_Pt50', 'massAve_Pairing03_Pt50', nBinsMass, 0, maxMass )
	deltaR_Pairing03_Pt60 	= TH1F('deltaR_Pairing03_Pt60', 'deltaR_Pairing03_Pt60', 100, 0, 5. )
	massAve_Pairing03_Pt60 	= TH1F('massAve_Pairing03_Pt60', 'massAve_Pairing03_Pt60', nBinsMass, 0, maxMass )
	deltaR_Pairing03_Pt70 	= TH1F('deltaR_Pairing03_Pt70', 'deltaR_Pairing03_Pt70', 100, 0, 5. )
	massAve_Pairing03_Pt70 	= TH1F('massAve_Pairing03_Pt70', 'massAve_Pairing03_Pt70', nBinsMass, 0, maxMass )
	deltaR_Pairing03_Pt80 	= TH1F('deltaR_Pairing03_Pt80', 'deltaR_Pairing03_Pt80', 100, 0, 5. )
	massAve_Pairing03_Pt80 	= TH1F('massAve_Pairing03_Pt80', 'massAve_Pairing03_Pt80', nBinsMass, 0, maxMass )
	deltaR_Pairing03_Pt100 	= TH1F('deltaR_Pairing03_Pt100', 'deltaR_Pairing03_Pt100', 100, 0, 5. )
	massAve_Pairing03_Pt100 	= TH1F('massAve_Pairing03_Pt100', 'massAve_Pairing03_Pt100', nBinsMass, 0, maxMass )

	deltaR_Pairing04 	= TH1F('deltaR_Pairing04', 'deltaR_Pairing04', 100, 0, 5. )
	massAve_Pairing04 	= TH1F('massAve_Pairing04', 'massAve_Pairing04', nBinsMass, 0, maxMass )
	deltaR_Pairing04_Pt50 	= TH1F('deltaR_Pairing04_Pt50', 'deltaR_Pairing04_Pt50', 100, 0, 5. )
	massAve_Pairing04_Pt50 	= TH1F('massAve_Pairing04_Pt50', 'massAve_Pairing04_Pt50', nBinsMass, 0, maxMass )
	deltaR_Pairing04_Pt60 	= TH1F('deltaR_Pairing04_Pt60', 'deltaR_Pairing04_Pt60', 100, 0, 5. )
	massAve_Pairing04_Pt60 	= TH1F('massAve_Pairing04_Pt60', 'massAve_Pairing04_Pt60', nBinsMass, 0, maxMass )
	deltaR_Pairing04_Pt70 	= TH1F('deltaR_Pairing04_Pt70', 'deltaR_Pairing04_Pt70', 100, 0, 5. )
	massAve_Pairing04_Pt70 	= TH1F('massAve_Pairing04_Pt70', 'massAve_Pairing04_Pt70', nBinsMass, 0, maxMass )
	deltaR_Pairing04_Pt80 	= TH1F('deltaR_Pairing04_Pt80', 'deltaR_Pairing04_Pt80', 100, 0, 5. )
	massAve_Pairing04_Pt80 	= TH1F('massAve_Pairing04_Pt80', 'massAve_Pairing04_Pt80', nBinsMass, 0, maxMass )
	deltaR_Pairing04_Pt100 	= TH1F('deltaR_Pairing04_Pt100', 'deltaR_Pairing04_Pt100', 100, 0, 5. )
	massAve_Pairing04_Pt100 	= TH1F('massAve_Pairing04_Pt100', 'massAve_Pairing04_Pt100', nBinsMass, 0, maxMass )

	deltaR_Pairing05 	= TH1F('deltaR_Pairing05', 'deltaR_Pairing05', 100, 0, 5. )
	massAve_Pairing05 	= TH1F('massAve_Pairing05', 'massAve_Pairing05', nBinsMass, 0, maxMass )
	deltaR_Pairing05_Pt50 	= TH1F('deltaR_Pairing05_Pt50', 'deltaR_Pairing05_Pt50', 100, 0, 5. )
	massAve_Pairing05_Pt50 	= TH1F('massAve_Pairing05_Pt50', 'massAve_Pairing05_Pt50', nBinsMass, 0, maxMass )
	deltaR_Pairing05_Pt60 	= TH1F('deltaR_Pairing05_Pt60', 'deltaR_Pairing05_Pt60', 100, 0, 5. )
	massAve_Pairing05_Pt60 	= TH1F('massAve_Pairing05_Pt60', 'massAve_Pairing05_Pt60', nBinsMass, 0, maxMass )
	deltaR_Pairing05_Pt70 	= TH1F('deltaR_Pairing05_Pt70', 'deltaR_Pairing05_Pt70', 100, 0, 5. )
	massAve_Pairing05_Pt70 	= TH1F('massAve_Pairing05_Pt70', 'massAve_Pairing05_Pt70', nBinsMass, 0, maxMass )
	deltaR_Pairing05_Pt80 	= TH1F('deltaR_Pairing05_Pt80', 'deltaR_Pairing05_Pt80', 100, 0, 5. )
	massAve_Pairing05_Pt80 	= TH1F('massAve_Pairing05_Pt80', 'massAve_Pairing05_Pt80', nBinsMass, 0, maxMass )
	deltaR_Pairing05_Pt100 	= TH1F('deltaR_Pairing05_Pt100', 'deltaR_Pairing05_Pt100', 100, 0, 5. )
	massAve_Pairing05_Pt100 	= TH1F('massAve_Pairing05_Pt100', 'massAve_Pairing05_Pt100', nBinsMass, 0, maxMass )

	deltaR_Pairing06 	= TH1F('deltaR_Pairing06', 'deltaR_Pairing06', 100, 0, 5. )
	massAve_Pairing06 	= TH1F('massAve_Pairing06', 'massAve_Pairing06', nBinsMass, 0, maxMass )
	deltaR_Pairing06_Pt50 	= TH1F('deltaR_Pairing06_Pt50', 'deltaR_Pairing06_Pt50', 100, 0, 5. )
	massAve_Pairing06_Pt50 	= TH1F('massAve_Pairing06_Pt50', 'massAve_Pairing06_Pt50', nBinsMass, 0, maxMass )
	deltaR_Pairing06_Pt60 	= TH1F('deltaR_Pairing06_Pt60', 'deltaR_Pairing06_Pt60', 100, 0, 5. )
	massAve_Pairing06_Pt60 	= TH1F('massAve_Pairing06_Pt60', 'massAve_Pairing06_Pt60', nBinsMass, 0, maxMass )
	deltaR_Pairing06_Pt70 	= TH1F('deltaR_Pairing06_Pt70', 'deltaR_Pairing06_Pt70', 100, 0, 5. )
	massAve_Pairing06_Pt70 	= TH1F('massAve_Pairing06_Pt70', 'massAve_Pairing06_Pt70', nBinsMass, 0, maxMass )
	deltaR_Pairing06_Pt80 	= TH1F('deltaR_Pairing06_Pt80', 'deltaR_Pairing06_Pt80', 100, 0, 5. )
	massAve_Pairing06_Pt80 	= TH1F('massAve_Pairing06_Pt80', 'massAve_Pairing06_Pt80', nBinsMass, 0, maxMass )
	deltaR_Pairing06_Pt100 	= TH1F('deltaR_Pairing06_Pt100', 'deltaR_Pairing06_Pt100', 100, 0, 5. )
	massAve_Pairing06_Pt100 	= TH1F('massAve_Pairing06_Pt100', 'massAve_Pairing06_Pt100', nBinsMass, 0, maxMass )

	deltaR_Pairing07 	= TH1F('deltaR_Pairing07', 'deltaR_Pairing07', 100, 0, 5. )
	massAve_Pairing07 	= TH1F('massAve_Pairing07', 'massAve_Pairing07', nBinsMass, 0, maxMass )
	deltaR_Pairing07_Pt50 	= TH1F('deltaR_Pairing07_Pt50', 'deltaR_Pairing07_Pt50', 100, 0, 5. )
	massAve_Pairing07_Pt50 	= TH1F('massAve_Pairing07_Pt50', 'massAve_Pairing07_Pt50', nBinsMass, 0, maxMass )
	deltaR_Pairing07_Pt60 	= TH1F('deltaR_Pairing07_Pt60', 'deltaR_Pairing07_Pt60', 100, 0, 5. )
	massAve_Pairing07_Pt60 	= TH1F('massAve_Pairing07_Pt60', 'massAve_Pairing07_Pt60', nBinsMass, 0, maxMass )
	deltaR_Pairing07_Pt70 	= TH1F('deltaR_Pairing07_Pt70', 'deltaR_Pairing07_Pt70', 100, 0, 5. )
	massAve_Pairing07_Pt70 	= TH1F('massAve_Pairing07_Pt70', 'massAve_Pairing07_Pt70', nBinsMass, 0, maxMass )
	deltaR_Pairing07_Pt80 	= TH1F('deltaR_Pairing07_Pt80', 'deltaR_Pairing07_Pt80', 100, 0, 5. )
	massAve_Pairing07_Pt80 	= TH1F('massAve_Pairing07_Pt80', 'massAve_Pairing07_Pt80', nBinsMass, 0, maxMass )
	deltaR_Pairing07_Pt100 	= TH1F('deltaR_Pairing07_Pt100', 'deltaR_Pairing07_Pt100', 100, 0, 5. )
	massAve_Pairing07_Pt100 	= TH1F('massAve_Pairing07_Pt100', 'massAve_Pairing07_Pt100', nBinsMass, 0, maxMass )

	deltaR_Pairing08 	= TH1F('deltaR_Pairing08', 'deltaR_Pairing08', 100, 0, 5. )
	massAve_Pairing08 	= TH1F('massAve_Pairing08', 'massAve_Pairing08', nBinsMass, 0, maxMass )
	deltaR_Pairing08_Pt50 	= TH1F('deltaR_Pairing08_Pt50', 'deltaR_Pairing08_Pt50', 100, 0, 5. )
	massAve_Pairing08_Pt50 	= TH1F('massAve_Pairing08_Pt50', 'massAve_Pairing08_Pt50', nBinsMass, 0, maxMass )
	deltaR_Pairing08_Pt60 	= TH1F('deltaR_Pairing08_Pt60', 'deltaR_Pairing08_Pt60', 100, 0, 5. )
	massAve_Pairing08_Pt60 	= TH1F('massAve_Pairing08_Pt60', 'massAve_Pairing08_Pt60', nBinsMass, 0, maxMass )
	deltaR_Pairing08_Pt70 	= TH1F('deltaR_Pairing08_Pt70', 'deltaR_Pairing08_Pt70', 100, 0, 5. )
	massAve_Pairing08_Pt70 	= TH1F('massAve_Pairing08_Pt70', 'massAve_Pairing08_Pt70', nBinsMass, 0, maxMass )
	deltaR_Pairing08_Pt80 	= TH1F('deltaR_Pairing08_Pt80', 'deltaR_Pairing08_Pt80', 100, 0, 5. )
	massAve_Pairing08_Pt80 	= TH1F('massAve_Pairing08_Pt80', 'massAve_Pairing08_Pt80', nBinsMass, 0, maxMass )
	deltaR_Pairing08_Pt100 	= TH1F('deltaR_Pairing08_Pt100', 'deltaR_Pairing08_Pt100', 100, 0, 5. )
	massAve_Pairing08_Pt100 	= TH1F('massAve_Pairing08_Pt100', 'massAve_Pairing08_Pt100', nBinsMass, 0, maxMass )

	deltaR_Pairing09 	= TH1F('deltaR_Pairing09', 'deltaR_Pairing09', 100, 0, 5. )
	massAve_Pairing09 	= TH1F('massAve_Pairing09', 'massAve_Pairing09', nBinsMass, 0, maxMass )
	deltaR_Pairing09_Pt50 	= TH1F('deltaR_Pairing09_Pt50', 'deltaR_Pairing09_Pt50', 100, 0, 5. )
	massAve_Pairing09_Pt50 	= TH1F('massAve_Pairing09_Pt50', 'massAve_Pairing09_Pt50', nBinsMass, 0, maxMass )
	deltaR_Pairing09_Pt60 	= TH1F('deltaR_Pairing09_Pt60', 'deltaR_Pairing09_Pt60', 100, 0, 5. )
	massAve_Pairing09_Pt60 	= TH1F('massAve_Pairing09_Pt60', 'massAve_Pairing09_Pt60', nBinsMass, 0, maxMass )
	deltaR_Pairing09_Pt70 	= TH1F('deltaR_Pairing09_Pt70', 'deltaR_Pairing09_Pt70', 100, 0, 5. )
	massAve_Pairing09_Pt70 	= TH1F('massAve_Pairing09_Pt70', 'massAve_Pairing09_Pt70', nBinsMass, 0, maxMass )
	deltaR_Pairing09_Pt80 	= TH1F('deltaR_Pairing09_Pt80', 'deltaR_Pairing09_Pt80', 100, 0, 5. )
	massAve_Pairing09_Pt80 	= TH1F('massAve_Pairing09_Pt80', 'massAve_Pairing09_Pt80', nBinsMass, 0, maxMass )
	deltaR_Pairing09_Pt100 	= TH1F('deltaR_Pairing09_Pt100', 'deltaR_Pairing09_Pt100', 100, 0, 5. )
	massAve_Pairing09_Pt100 	= TH1F('massAve_Pairing09_Pt100', 'massAve_Pairing09_Pt100', nBinsMass, 0, maxMass )

	deltaR_Pairing10 	= TH1F('deltaR_Pairing10', 'deltaR_Pairing10', 100, 0, 5. )
	massAve_Pairing10 	= TH1F('massAve_Pairing10', 'massAve_Pairing10', nBinsMass, 0, maxMass )
	deltaR_Pairing10_Pt50 	= TH1F('deltaR_Pairing10_Pt50', 'deltaR_Pairing10_Pt50', 100, 0, 5. )
	massAve_Pairing10_Pt50 	= TH1F('massAve_Pairing10_Pt50', 'massAve_Pairing10_Pt50', nBinsMass, 0, maxMass )
	deltaR_Pairing10_Pt60 	= TH1F('deltaR_Pairing10_Pt60', 'deltaR_Pairing10_Pt60', 100, 0, 5. )
	massAve_Pairing10_Pt60 	= TH1F('massAve_Pairing10_Pt60', 'massAve_Pairing10_Pt60', nBinsMass, 0, maxMass )
	deltaR_Pairing10_Pt70 	= TH1F('deltaR_Pairing10_Pt70', 'deltaR_Pairing10_Pt70', 100, 0, 5. )
	massAve_Pairing10_Pt70 	= TH1F('massAve_Pairing10_Pt70', 'massAve_Pairing10_Pt70', nBinsMass, 0, maxMass )
	deltaR_Pairing10_Pt80 	= TH1F('deltaR_Pairing10_Pt80', 'deltaR_Pairing10_Pt80', 100, 0, 5. )
	massAve_Pairing10_Pt80 	= TH1F('massAve_Pairing10_Pt80', 'massAve_Pairing10_Pt80', nBinsMass, 0, maxMass )
	deltaR_Pairing10_Pt100 	= TH1F('deltaR_Pairing10_Pt100', 'deltaR_Pairing10_Pt100', 100, 0, 5. )
	massAve_Pairing10_Pt100 	= TH1F('massAve_Pairing10_Pt100', 'massAve_Pairing10_Pt100', nBinsMass, 0, maxMass )

	deltaR_Pairing11 	= TH1F('deltaR_Pairing11', 'deltaR_Pairing11', 100, 0, 5. )
	massAve_Pairing11 	= TH1F('massAve_Pairing11', 'massAve_Pairing11', nBinsMass, 0, maxMass )
	deltaR_Pairing11_Pt50 	= TH1F('deltaR_Pairing11_Pt50', 'deltaR_Pairing11_Pt50', 100, 0, 5. )
	massAve_Pairing11_Pt50 	= TH1F('massAve_Pairing11_Pt50', 'massAve_Pairing11_Pt50', nBinsMass, 0, maxMass )
	deltaR_Pairing11_Pt60 	= TH1F('deltaR_Pairing11_Pt60', 'deltaR_Pairing11_Pt60', 100, 0, 5. )
	massAve_Pairing11_Pt60 	= TH1F('massAve_Pairing11_Pt60', 'massAve_Pairing11_Pt60', nBinsMass, 0, maxMass )
	deltaR_Pairing11_Pt70 	= TH1F('deltaR_Pairing11_Pt70', 'deltaR_Pairing11_Pt70', 100, 0, 5. )
	massAve_Pairing11_Pt70 	= TH1F('massAve_Pairing11_Pt70', 'massAve_Pairing11_Pt70', nBinsMass, 0, maxMass )
	deltaR_Pairing11_Pt80 	= TH1F('deltaR_Pairing11_Pt80', 'deltaR_Pairing11_Pt80', 100, 0, 5. )
	massAve_Pairing11_Pt80 	= TH1F('massAve_Pairing11_Pt80', 'massAve_Pairing11_Pt80', nBinsMass, 0, maxMass )
	deltaR_Pairing11_Pt100 	= TH1F('deltaR_Pairing11_Pt100', 'deltaR_Pairing11_Pt100', 100, 0, 5. )
	massAve_Pairing11_Pt100 	= TH1F('massAve_Pairing11_Pt100', 'massAve_Pairing11_Pt100', nBinsMass, 0, maxMass )

	deltaR_Pairing12 	= TH1F('deltaR_Pairing12', 'deltaR_Pairing12', 100, 0, 5. )
	massAve_Pairing12 	= TH1F('massAve_Pairing12', 'massAve_Pairing12', nBinsMass, 0, maxMass )
	deltaR_Pairing12_Pt50 	= TH1F('deltaR_Pairing12_Pt50', 'deltaR_Pairing12_Pt50', 100, 0, 5. )
	massAve_Pairing12_Pt50 	= TH1F('massAve_Pairing12_Pt50', 'massAve_Pairing12_Pt50', nBinsMass, 0, maxMass )
	deltaR_Pairing12_Pt60 	= TH1F('deltaR_Pairing12_Pt60', 'deltaR_Pairing12_Pt60', 100, 0, 5. )
	massAve_Pairing12_Pt60 	= TH1F('massAve_Pairing12_Pt60', 'massAve_Pairing12_Pt60', nBinsMass, 0, maxMass )
	deltaR_Pairing12_Pt70 	= TH1F('deltaR_Pairing12_Pt70', 'deltaR_Pairing12_Pt70', 100, 0, 5. )
	massAve_Pairing12_Pt70 	= TH1F('massAve_Pairing12_Pt70', 'massAve_Pairing12_Pt70', nBinsMass, 0, maxMass )
	deltaR_Pairing12_Pt80 	= TH1F('deltaR_Pairing12_Pt80', 'deltaR_Pairing12_Pt80', 100, 0, 5. )
	massAve_Pairing12_Pt80 	= TH1F('massAve_Pairing12_Pt80', 'massAve_Pairing12_Pt80', nBinsMass, 0, maxMass )
	deltaR_Pairing12_Pt100 	= TH1F('deltaR_Pairing12_Pt100', 'deltaR_Pairing12_Pt100', 100, 0, 5. )
	massAve_Pairing12_Pt100 	= TH1F('massAve_Pairing12_Pt100', 'massAve_Pairing12_Pt100', nBinsMass, 0, maxMass )

	deltaR_Pairing13 	= TH1F('deltaR_Pairing13', 'deltaR_Pairing13', 100, 0, 5. )
	massAve_Pairing13 	= TH1F('massAve_Pairing13', 'massAve_Pairing13', nBinsMass, 0, maxMass )
	deltaR_Pairing13_Pt50 	= TH1F('deltaR_Pairing13_Pt50', 'deltaR_Pairing13_Pt50', 100, 0, 5. )
	massAve_Pairing13_Pt50 	= TH1F('massAve_Pairing13_Pt50', 'massAve_Pairing13_Pt50', nBinsMass, 0, maxMass )
	deltaR_Pairing13_Pt60 	= TH1F('deltaR_Pairing13_Pt60', 'deltaR_Pairing13_Pt60', 100, 0, 5. )
	massAve_Pairing13_Pt60 	= TH1F('massAve_Pairing13_Pt60', 'massAve_Pairing13_Pt60', nBinsMass, 0, maxMass )
	deltaR_Pairing13_Pt70 	= TH1F('deltaR_Pairing13_Pt70', 'deltaR_Pairing13_Pt70', 100, 0, 5. )
	massAve_Pairing13_Pt70 	= TH1F('massAve_Pairing13_Pt70', 'massAve_Pairing13_Pt70', nBinsMass, 0, maxMass )
	deltaR_Pairing13_Pt80 	= TH1F('deltaR_Pairing13_Pt80', 'deltaR_Pairing13_Pt80', 100, 0, 5. )
	massAve_Pairing13_Pt80 	= TH1F('massAve_Pairing13_Pt80', 'massAve_Pairing13_Pt80', nBinsMass, 0, maxMass )
	deltaR_Pairing13_Pt100 	= TH1F('deltaR_Pairing13_Pt100', 'deltaR_Pairing13_Pt100', 100, 0, 5. )
	massAve_Pairing13_Pt100 	= TH1F('massAve_Pairing13_Pt100', 'massAve_Pairing13_Pt100', nBinsMass, 0, maxMass )

	'''
	massAve_Pairing 	= TH1F('massAve_Pairing', 'massAve_Pairing', nBinsMass, 0, maxMass )
	massAve_DeltaRBest 	= TH1F('massAve_DeltaRBest', 'massAve_DeltaRBest', nBinsMass, 0, maxMass )
	massAve_DeltaR 	= TH1F('massAve_DeltaR', 'massAve_DeltaR', nBinsMass, 0, maxMass )
	massAve_DeltaRCosTheta 	= TH1F('massAve_DeltaRCosTheta', 'massAve_DeltaRCosTheta', nBinsMass, 0, maxMass )
	massAve_DeltaRCosThetaDeltaEta 	= TH1F('massAve_DeltaRCosThetaDeltaEta', 'massAve_DeltaRCosThetaDeltaEta', nBinsMass, 0, maxMass )
	massAve_DeltaRCosThetaDeltaEtaMassPar 	= TH1F('massAve_DeltaRCosThetaDeltaEtaMassPar', 'massAve_DeltaRCosThetaDeltaEtaMassPar', nBinsMass, 0, maxMass )
	massAve_DeltaEta 	= TH1F('massAve_DeltaEta', 'massAve_DeltaEta', nBinsMass, 0, maxMass )
	massAve_MassPar 	= TH1F('massAve_MassPar', 'massAve_MassPar', nBinsMass, 0, maxMass )
	massAve_CosTheta 	= TH1F('massAve_CosTheta', 'massAve_CosTheta', nBinsMass, 0, maxMass )
=======
	deltaR_Pairing08 	= TH1F('deltaR_Pairing08', 'deltaR_Pairing08', 100, 0, 5. )
	deltaR_Pairing09 	= TH1F('deltaR_Pairing09', 'deltaR_Pairing09', 100, 0, 5. )
	deltaR_Pairing10 	= TH1F('deltaR_Pairing10', 'deltaR_Pairing10', 100, 0, 5. )
	deltaR_Pairing11 	= TH1F('deltaR_Pairing11', 'deltaR_Pairing11', 100, 0, 5. )
	deltaR_Pairing12 	= TH1F('deltaR_Pairing12', 'deltaR_Pairing12', 100, 0, 5. )
	massAve_Pairing 	= TH1F('massAve_Pairing', 'massAve_Pairing', nBinsMass, 0, maxMass )
	massAve_DeltaRBest 	= TH1F('massAve_DeltaRBest', 'massAve_DeltaRBest', nBinsMass, 0, maxMass )
	massAve_DeltaR 	= TH1F('massAve_DeltaR', 'massAve_DeltaR', nBinsMass, 0, maxMass )
	massAve_DeltaEta 	= TH1F('massAve_DeltaEta', 'massAve_DeltaEta', nBinsMass, 0, maxMass )
	massAve_MassPar 	= TH1F('massAve_MassPar', 'massAve_MassPar', nBinsMass, 0, maxMass )
	massAve_EtaMassParDeltaR 	= TH1F('massAve_EtaMassParDeltaR', 'massAve_EtaMassParDeltaR', nBinsMass, 0, maxMass )
>>>>>>> 1ed1f13e9a39e2d9412a067d05462ef0c0cedbeb
	massAve_Delta 	= TH1F('massAve_Delta', 'massAve_Delta', nBinsMass, 0, maxMass )
	massAve_DeltaDeltaR 	= TH1F('massAve_DeltaDeltaR', 'massAve_DeltaDeltaR', nBinsMass, 0, maxMass )
	massAve_DeltaDeltaEta 	= TH1F('massAve_DeltaDeltaEta', 'massAve_DeltaDeltaEta', nBinsMass, 0, maxMass )
	massAve_DeltaMassPar 	= TH1F('massAve_DeltaMassPar', 'massAve_DeltaMassPar', nBinsMass, 0, maxMass )
<<<<<<< HEAD
	massAve_Delta_cutJetPt 	= TH1F('massAve_Delta_cutJetPt', 'massAve_Delta_cutJetPt', nBinsMass, 0, maxMass )
	massAve_DeltaDeltaEta_cutJetPt 	= TH1F('massAve_DeltaDeltaEta_cutJetPt', 'massAve_DeltaDeltaEta_cutJetPt', nBinsMass, 0, maxMass )
	massAve_DeltaMassPar_cutJetPt 	= TH1F('massAve_DeltaMassPar_cutJetPt', 'massAve_DeltaMassPar_cutJetPt', nBinsMass, 0, maxMass )
=======
	massAve_DeltaEtaMassParDeltaR 	= TH1F('massAve_DeltaEtaMassParDeltaR', 'massAve_DeltaEtaMassParDeltaR', nBinsMass, 0, maxMass )
	massAve_CosTheta 	= TH1F('massAve_CosTheta', 'massAve_CosTheta', nBinsMass, 0, maxMass )
	massAve_CosThetaDeltaR 	= TH1F('massAve_CosThetaDeltaR', 'massAve_CosThetaDeltaR', nBinsMass, 0, maxMass )
	massAve_CosThetaDeltaEta 	= TH1F('massAve_CosThetaDeltaEta', 'massAve_CosThetaDeltaEta', nBinsMass, 0, maxMass )
	massAve_CosThetaMassPar 	= TH1F('massAve_CosThetaMassPar', 'massAve_CosThetaMassPar', nBinsMass, 0, maxMass )
	massAve_CosThetaEtaMassParDeltaR 	= TH1F('massAve_CosThetaEtaMassParDeltaR', 'massAve_CosThetaEtaMassParDeltaR', nBinsMass, 0, maxMass )
>>>>>>> 1ed1f13e9a39e2d9412a067d05462ef0c0cedbeb
	deltaR_Pairing 	= TH1F('deltaR_Pairing', 'deltaR_Pairing', 100, 0, 5. )
	deltaEtaDijet_Pairing 	= TH1F('deltaEtaDijet_Pairing', 'deltaEtaDijet_Pairing', 100, 0, 5. )
	massPairing_Pairing 	= TH1F('massPairing_Pairing', 'massPairing_Pairing', 20, 0, 1. )
	deltaEtaDijet1_Pairing 	= TH1F('deltaEtaDijet1_Pairing', 'deltaEtaDijet1_Pairing', 100, 0, 5. )
	deltaEtaDijet2_Pairing 	= TH1F('deltaEtaDijet2_Pairing', 'deltaEtaDijet2_Pairing', 100, 0, 5. )
	deltaEtaBest_Pairing 	= TH1F('deltaEtaBest_Pairing', 'deltaEtaBest_Pairing', 100, 0, 5. )
	deltaPhiDijet_Pairing 	= TH1F('deltaPhiDijet_Pairing', 'deltaPhiDijet_Pairing', 100, 0, 5. )
	deltaPhiBest_Pairing 	= TH1F('deltaPhiBest_Pairing', 'deltaPhiBest_Pairing', 100, 0, 5. )
	deltaRDijet_Pairing 	= TH1F('deltaRDijet_Pairing', 'deltaRDijet_Pairing', 100, 0, 5. )
	deltaRBest_Pairing 	= TH1F('deltaRBest_Pairing', 'deltaRBest_Pairing', 100, 0, 5. )
	cosThetaStar1_Pairing 	= TH1F('cosThetaStar1_Pairing', 'cosThetaStar1_Pairing', 20, 0, 1. )
	cosThetaStar2_Pairing 	= TH1F('cosThetaStar2_Pairing', 'cosThetaStar2_Pairing', 20, 0, 1. )
<<<<<<< HEAD
	'''
=======


	massAve_Pairing09 	= TH1F('massAve_Pairing09', 'massAve_Pairing09', nBinsMass, 0, maxMass )
	massAve_DeltaRBest09	= TH1F('massAve_DeltaRBest09', 'massAve_DeltaRBest09', nBinsMass, 0, maxMass )
	massAve_DeltaR09	= TH1F('massAve_DeltaR09', 'massAve_DeltaR09', nBinsMass, 0, maxMass )
	massAve_DeltaEta09	= TH1F('massAve_DeltaEta09', 'massAve_DeltaEta09', nBinsMass, 0, maxMass )
	massAve_MassPar09	= TH1F('massAve_MassPar09', 'massAve_MassPar09', nBinsMass, 0, maxMass )
	massAve_EtaMassParDeltaR09	= TH1F('massAve_EtaMassParDeltaR09', 'massAve_EtaMassParDeltaR09', nBinsMass, 0, maxMass )
	massAve_Delta09	= TH1F('massAve_Delta09', 'massAve_Delta09', nBinsMass, 0, maxMass )
	massAve_DeltaDeltaR09	= TH1F('massAve_DeltaDeltaR09', 'massAve_DeltaDeltaR09', nBinsMass, 0, maxMass )
	massAve_DeltaDeltaEta09	= TH1F('massAve_DeltaDeltaEta09', 'massAve_DeltaDeltaEta09', nBinsMass, 0, maxMass )
	massAve_DeltaMassPar09	= TH1F('massAve_DeltaMassPar09', 'massAve_DeltaMassPar09', nBinsMass, 0, maxMass )
	massAve_DeltaEtaMassParDeltaR09	= TH1F('massAve_DeltaEtaMassParDeltaR09', 'massAve_DeltaEtaMassParDeltaR09', nBinsMass, 0, maxMass )
	massAve_CosTheta09	= TH1F('massAve_CosTheta09', 'massAve_CosTheta09', nBinsMass, 0, maxMass )
	massAve_CosThetaDeltaR09	= TH1F('massAve_CosThetaDeltaR09', 'massAve_CosThetaDeltaR09', nBinsMass, 0, maxMass )
	massAve_CosThetaDeltaEta09	= TH1F('massAve_CosThetaDeltaEta09', 'massAve_CosThetaDeltaEta09', nBinsMass, 0, maxMass )
	massAve_CosThetaMassPar09	= TH1F('massAve_CosThetaMassPar09', 'massAve_CosThetaMassPar09', nBinsMass, 0, maxMass )
	massAve_CosThetaEtaMassParDeltaR09	= TH1F('massAve_CosThetaEtaMassParDeltaR09', 'massAve_CosThetaEtaMassParDeltaR09', nBinsMass, 0, maxMass )
	deltaEtaDijet_Pairing09 	= TH1F('deltaEtaDijet_Pairing09', 'deltaEtaDijet_Pairing09', 100, 0, 5. )
	massPairing_Pairing09 	= TH1F('massPairing_Pairing09', 'massPairing_Pairing09', 20, 0, 1. )
	deltaEtaDijet1_Pairing09 	= TH1F('deltaEtaDijet1_Pairing09', 'deltaEtaDijet1_Pairing09', 100, 0, 5. )
	deltaEtaDijet2_Pairing09 	= TH1F('deltaEtaDijet2_Pairing09', 'deltaEtaDijet2_Pairing09', 100, 0, 5. )
	deltaEtaBest_Pairing09 	= TH1F('deltaEtaBest_Pairing09', 'deltaEtaBest_Pairing09', 100, 0, 5. )
	deltaPhiDijet_Pairing09 	= TH1F('deltaPhiDijet_Pairing09', 'deltaPhiDijet_Pairing09', 100, 0, 5. )
	deltaPhiBest_Pairing09 	= TH1F('deltaPhiBest_Pairing09', 'deltaPhiBest_Pairing09', 100, 0, 5. )
	deltaRDijet_Pairing09 	= TH1F('deltaRDijet_Pairing09', 'deltaRDijet_Pairing09', 100, 0, 5. )
	deltaRBest_Pairing09 	= TH1F('deltaRBest_Pairing09', 'deltaRBest_Pairing09', 100, 0, 5. )
	cosThetaStar1_Pairing09 	= TH1F('cosThetaStar1_Pairing09', 'cosThetaStar1_Pairing09', 20, 0, 1. )
	cosThetaStar2_Pairing09 	= TH1F('cosThetaStar2_Pairing09', 'cosThetaStar2_Pairing09', 20, 0, 1. )
>>>>>>> 1ed1f13e9a39e2d9412a067d05462ef0c0cedbeb

	###################################### Get GenTree 
	events = inputFile.Get( 'RUNATree/RUNATree' )
	numEntries = events.GetEntriesFast()

	print '------> Number of events: '+str(numEntries)
	d = 0
	newLumi = 0
	tmpLumi = 0
	eventsRaw = eventsHT = eventsPassed = eventsDijet = eventsMassAsym = eventsDEta = eventsDEtaSubjet = eventsDEtaTau21 = eventsDEtaTau31 = eventsCosTheta = eventsTau21 = eventsTau21CosTheta = eventsTau21CosThetaDEta = 0
	for i in xrange(numEntries):
		events.GetEntry(i)
		eventsRaw += 1

		#---- progress of the reading --------
		fraction = 10.*i/(1.*numEntries)
		if TMath.FloorNint(fraction) > d: print str(10*TMath.FloorNint(fraction))+'%' 
		d = TMath.FloorNint(fraction)

		#---- progress of the reading --------
		Run      = events.run
		Lumi     = events.lumi
		NumEvent = events.event
		#print 'Entry ', Run, ':', Lumi, ':', NumEvent

		HT		= events.HT
		numJets		= events.numJets
		numPV           = events.numPV
		puWeight	 = events.puWeight
		lumiWeight	 = events.lumiWeight
		HT		 = events.HT
		mass1		 = events.mass1
		mass2		 = events.mass2
		avgMass		 = events.avgMass
		delta1		 = events.delta1
		delta2		 = events.delta2
		massRes		 = events.massRes
		eta1		 = events.eta1
		eta2		 = events.eta2
		deltaEta	 = events.deltaEta
		jetsPt		 = events.jetsPt
		jetsEta		 = events.jetsEta
		jetsPhi		 = events.jetsPhi
		jetsE		 = events.jetsE

<<<<<<< HEAD
		scale = 1265* puWeight * lumiWeight * 4.64
=======
		scale = 1265* puWeight * lumiWeight
>>>>>>> 1ed1f13e9a39e2d9412a067d05462ef0c0cedbeb
		j1 = TLorentzVector()
		j2 = TLorentzVector()
		j3 = TLorentzVector()
		j4 = TLorentzVector()
		massPairing = {}
<<<<<<< HEAD
		#if ( (len(jetsPt) == 4 ) and ( jetsPt[3] > 60 ) ):
=======
>>>>>>> 1ed1f13e9a39e2d9412a067d05462ef0c0cedbeb
		if (len(jetsPt) == 4 ):

			tmpj1 = TLorentzVector()
			tmpj2 = TLorentzVector()
			tmpj3 = TLorentzVector()
			tmpj4 = TLorentzVector()
			tmpj1.SetPtEtaPhiE( jetsPt[0], jetsEta[0], jetsPhi[0], jetsE[0] )
			tmpj2.SetPtEtaPhiE( jetsPt[1], jetsEta[1], jetsPhi[1], jetsE[1] )
			tmpj3.SetPtEtaPhiE( jetsPt[2], jetsEta[2], jetsPhi[2], jetsE[2] )
			tmpj4.SetPtEtaPhiE( jetsPt[3], jetsEta[3], jetsPhi[3], jetsE[3] )

<<<<<<< HEAD
			pairoff03 = Pairing( tmpj1, tmpj2, tmpj3, tmpj4, 0.3 )
			pairoff04 = Pairing( tmpj1, tmpj2, tmpj3, tmpj4, 0.4 )
			pairoff05 = Pairing( tmpj1, tmpj2, tmpj3, tmpj4, 0.5 )
			pairoff06 = Pairing( tmpj1, tmpj2, tmpj3, tmpj4, 0.6 )
			pairoff07 = Pairing( tmpj1, tmpj2, tmpj3, tmpj4, 0.7 )
=======
>>>>>>> 1ed1f13e9a39e2d9412a067d05462ef0c0cedbeb
			pairoff08 = Pairing( tmpj1, tmpj2, tmpj3, tmpj4, 0.8 )
			pairoff09 = Pairing( tmpj1, tmpj2, tmpj3, tmpj4, 0.9 )
			pairoff10 = Pairing( tmpj1, tmpj2, tmpj3, tmpj4, 1.0 )
			pairoff11 = Pairing( tmpj1, tmpj2, tmpj3, tmpj4, 1.1 )
			pairoff12 = Pairing( tmpj1, tmpj2, tmpj3, tmpj4, 1.2 )
<<<<<<< HEAD
			pairoff13 = Pairing( tmpj1, tmpj2, tmpj3, tmpj4, 1.3 )
			
			if pairoff03[0]: 
				deltaR_Pairing03.Fill( pairoff03[5] )
				massAve_Pairing03.Fill( ( ( ( pairoff03[1] + pairoff03[2] ).M() + ( pairoff03[3] + pairoff03[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 50 ):
					deltaR_Pairing03_Pt50.Fill( pairoff03[5] )
					massAve_Pairing03_Pt50.Fill( ( ( ( pairoff03[1] + pairoff03[2] ).M() + ( pairoff03[3] + pairoff03[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 60 ):
					deltaR_Pairing03_Pt60.Fill( pairoff03[5] )
					massAve_Pairing03_Pt60.Fill( ( ( ( pairoff03[1] + pairoff03[2] ).M() + ( pairoff03[3] + pairoff03[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 70 ):
					deltaR_Pairing03_Pt70.Fill( pairoff03[5] )
					massAve_Pairing03_Pt70.Fill( ( ( ( pairoff03[1] + pairoff03[2] ).M() + ( pairoff03[3] + pairoff03[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 80 ):
					deltaR_Pairing03_Pt80.Fill( pairoff03[5] )
					massAve_Pairing03_Pt80.Fill( ( ( ( pairoff03[1] + pairoff03[2] ).M() + ( pairoff03[3] + pairoff03[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 100 ):
					deltaR_Pairing03_Pt100.Fill( pairoff03[5] )
					massAve_Pairing03_Pt100.Fill( ( ( ( pairoff03[1] + pairoff03[2] ).M() + ( pairoff03[3] + pairoff03[4] ).M() ) / 2 ), scale )
			if pairoff04[0]: 
				deltaR_Pairing04.Fill( pairoff04[5] )
				massAve_Pairing04.Fill( ( ( ( pairoff04[1] + pairoff04[2] ).M() + ( pairoff04[3] + pairoff04[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 50 ):
					deltaR_Pairing04_Pt50.Fill( pairoff04[5] )
					massAve_Pairing04_Pt50.Fill( ( ( ( pairoff04[1] + pairoff04[2] ).M() + ( pairoff04[3] + pairoff04[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 60 ):
					deltaR_Pairing04_Pt60.Fill( pairoff04[5] )
					massAve_Pairing04_Pt60.Fill( ( ( ( pairoff04[1] + pairoff04[2] ).M() + ( pairoff04[3] + pairoff04[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 70 ):
					deltaR_Pairing04_Pt70.Fill( pairoff04[5] )
					massAve_Pairing04_Pt70.Fill( ( ( ( pairoff04[1] + pairoff04[2] ).M() + ( pairoff04[3] + pairoff04[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 80 ):
					deltaR_Pairing04_Pt80.Fill( pairoff04[5] )
					massAve_Pairing04_Pt80.Fill( ( ( ( pairoff04[1] + pairoff04[2] ).M() + ( pairoff04[3] + pairoff04[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 100 ):
					deltaR_Pairing04_Pt100.Fill( pairoff04[5] )
					massAve_Pairing04_Pt100.Fill( ( ( ( pairoff04[1] + pairoff04[2] ).M() + ( pairoff04[3] + pairoff04[4] ).M() ) / 2 ), scale )
			if pairoff05[0]: 
				deltaR_Pairing05.Fill( pairoff05[5] )
				massAve_Pairing05.Fill( ( ( ( pairoff05[1] + pairoff05[2] ).M() + ( pairoff05[3] + pairoff05[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 50 ):
					deltaR_Pairing05_Pt50.Fill( pairoff05[5] )
					massAve_Pairing05_Pt50.Fill( ( ( ( pairoff05[1] + pairoff05[2] ).M() + ( pairoff05[3] + pairoff05[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 60 ):
					deltaR_Pairing05_Pt60.Fill( pairoff05[5] )
					massAve_Pairing05_Pt60.Fill( ( ( ( pairoff05[1] + pairoff05[2] ).M() + ( pairoff05[3] + pairoff05[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 70 ):
					deltaR_Pairing05_Pt70.Fill( pairoff05[5] )
					massAve_Pairing05_Pt70.Fill( ( ( ( pairoff05[1] + pairoff05[2] ).M() + ( pairoff05[3] + pairoff05[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 80 ):
					deltaR_Pairing05_Pt80.Fill( pairoff05[5] )
					massAve_Pairing05_Pt80.Fill( ( ( ( pairoff05[1] + pairoff05[2] ).M() + ( pairoff05[3] + pairoff05[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 100 ):
					deltaR_Pairing05_Pt100.Fill( pairoff05[5] )
					massAve_Pairing05_Pt100.Fill( ( ( ( pairoff05[1] + pairoff05[2] ).M() + ( pairoff05[3] + pairoff05[4] ).M() ) / 2 ), scale )
			if pairoff06[0]: 
				deltaR_Pairing06.Fill( pairoff06[5] )
				massAve_Pairing06.Fill( ( ( ( pairoff06[1] + pairoff06[2] ).M() + ( pairoff06[3] + pairoff06[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 50 ):
					deltaR_Pairing06_Pt50.Fill( pairoff06[5] )
					massAve_Pairing06_Pt50.Fill( ( ( ( pairoff06[1] + pairoff06[2] ).M() + ( pairoff06[3] + pairoff06[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 60 ):
					deltaR_Pairing06_Pt60.Fill( pairoff06[5] )
					massAve_Pairing06_Pt60.Fill( ( ( ( pairoff06[1] + pairoff06[2] ).M() + ( pairoff06[3] + pairoff06[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 70 ):
					deltaR_Pairing06_Pt70.Fill( pairoff06[5] )
					massAve_Pairing06_Pt70.Fill( ( ( ( pairoff06[1] + pairoff06[2] ).M() + ( pairoff06[3] + pairoff06[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 80 ):
					deltaR_Pairing06_Pt80.Fill( pairoff06[5] )
					massAve_Pairing06_Pt80.Fill( ( ( ( pairoff06[1] + pairoff06[2] ).M() + ( pairoff06[3] + pairoff06[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 100 ):
					deltaR_Pairing06_Pt100.Fill( pairoff06[5] )
					massAve_Pairing06_Pt100.Fill( ( ( ( pairoff06[1] + pairoff06[2] ).M() + ( pairoff06[3] + pairoff06[4] ).M() ) / 2 ), scale )
			if pairoff07[0]: 
				deltaR_Pairing07.Fill( pairoff07[5] )
				massAve_Pairing07.Fill( ( ( ( pairoff07[1] + pairoff07[2] ).M() + ( pairoff07[3] + pairoff07[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 50 ):
					deltaR_Pairing07_Pt50.Fill( pairoff07[5] )
					massAve_Pairing07_Pt50.Fill( ( ( ( pairoff07[1] + pairoff07[2] ).M() + ( pairoff07[3] + pairoff07[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 60 ):
					deltaR_Pairing07_Pt60.Fill( pairoff07[5] )
					massAve_Pairing07_Pt60.Fill( ( ( ( pairoff07[1] + pairoff07[2] ).M() + ( pairoff07[3] + pairoff07[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 70 ):
					deltaR_Pairing07_Pt70.Fill( pairoff07[5] )
					massAve_Pairing07_Pt70.Fill( ( ( ( pairoff07[1] + pairoff07[2] ).M() + ( pairoff07[3] + pairoff07[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 80 ):
					deltaR_Pairing07_Pt80.Fill( pairoff07[5] )
					massAve_Pairing07_Pt80.Fill( ( ( ( pairoff07[1] + pairoff07[2] ).M() + ( pairoff07[3] + pairoff07[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 100 ):
					deltaR_Pairing07_Pt100.Fill( pairoff07[5] )
					massAve_Pairing07_Pt100.Fill( ( ( ( pairoff07[1] + pairoff07[2] ).M() + ( pairoff07[3] + pairoff07[4] ).M() ) / 2 ), scale )
			if pairoff08[0]: 
				deltaR_Pairing08.Fill( pairoff08[5] )
				massAve_Pairing08.Fill( ( ( ( pairoff08[1] + pairoff08[2] ).M() + ( pairoff08[3] + pairoff08[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 50 ):
					deltaR_Pairing08_Pt50.Fill( pairoff08[5] )
					massAve_Pairing08_Pt50.Fill( ( ( ( pairoff08[1] + pairoff08[2] ).M() + ( pairoff08[3] + pairoff08[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 60 ):
					deltaR_Pairing08_Pt60.Fill( pairoff08[5] )
					massAve_Pairing08_Pt60.Fill( ( ( ( pairoff08[1] + pairoff08[2] ).M() + ( pairoff08[3] + pairoff08[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 70 ):
					deltaR_Pairing08_Pt70.Fill( pairoff08[5] )
					massAve_Pairing08_Pt70.Fill( ( ( ( pairoff08[1] + pairoff08[2] ).M() + ( pairoff08[3] + pairoff08[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 80 ):
					deltaR_Pairing08_Pt80.Fill( pairoff08[5] )
					massAve_Pairing08_Pt80.Fill( ( ( ( pairoff08[1] + pairoff08[2] ).M() + ( pairoff08[3] + pairoff08[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 100 ):
					deltaR_Pairing08_Pt100.Fill( pairoff08[5] )
					massAve_Pairing08_Pt100.Fill( ( ( ( pairoff08[1] + pairoff08[2] ).M() + ( pairoff08[3] + pairoff08[4] ).M() ) / 2 ), scale )
			if pairoff09[0]: 
				deltaR_Pairing09.Fill( pairoff09[5] )
				massAve_Pairing09.Fill( ( ( ( pairoff09[1] + pairoff09[2] ).M() + ( pairoff09[3] + pairoff09[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 50 ):
					deltaR_Pairing09_Pt50.Fill( pairoff09[5] )
					massAve_Pairing09_Pt50.Fill( ( ( ( pairoff09[1] + pairoff09[2] ).M() + ( pairoff09[3] + pairoff09[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 60 ):
					deltaR_Pairing09_Pt60.Fill( pairoff09[5] )
					massAve_Pairing09_Pt60.Fill( ( ( ( pairoff09[1] + pairoff09[2] ).M() + ( pairoff09[3] + pairoff09[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 70 ):
					deltaR_Pairing09_Pt70.Fill( pairoff09[5] )
					massAve_Pairing09_Pt70.Fill( ( ( ( pairoff09[1] + pairoff09[2] ).M() + ( pairoff09[3] + pairoff09[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 80 ):
					deltaR_Pairing09_Pt80.Fill( pairoff09[5] )
					massAve_Pairing09_Pt80.Fill( ( ( ( pairoff09[1] + pairoff09[2] ).M() + ( pairoff09[3] + pairoff09[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 100 ):
					deltaR_Pairing09_Pt100.Fill( pairoff09[5] )
					massAve_Pairing09_Pt100.Fill( ( ( ( pairoff09[1] + pairoff09[2] ).M() + ( pairoff09[3] + pairoff09[4] ).M() ) / 2 ), scale )
			if pairoff10[0]: 
				deltaR_Pairing10.Fill( pairoff10[5] )
				massAve_Pairing10.Fill( ( ( ( pairoff10[1] + pairoff10[2] ).M() + ( pairoff10[3] + pairoff10[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 50 ):
					deltaR_Pairing10_Pt50.Fill( pairoff10[5] )
					massAve_Pairing10_Pt50.Fill( ( ( ( pairoff10[1] + pairoff10[2] ).M() + ( pairoff10[3] + pairoff10[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 60 ):
					deltaR_Pairing10_Pt60.Fill( pairoff10[5] )
					massAve_Pairing10_Pt60.Fill( ( ( ( pairoff10[1] + pairoff10[2] ).M() + ( pairoff10[3] + pairoff10[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 70 ):
					deltaR_Pairing10_Pt70.Fill( pairoff10[5] )
					massAve_Pairing10_Pt70.Fill( ( ( ( pairoff10[1] + pairoff10[2] ).M() + ( pairoff10[3] + pairoff10[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 80 ):
					deltaR_Pairing10_Pt80.Fill( pairoff10[5] )
					massAve_Pairing10_Pt80.Fill( ( ( ( pairoff10[1] + pairoff10[2] ).M() + ( pairoff10[3] + pairoff10[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 100 ):
					deltaR_Pairing10_Pt100.Fill( pairoff10[5] )
					massAve_Pairing10_Pt100.Fill( ( ( ( pairoff10[1] + pairoff10[2] ).M() + ( pairoff10[3] + pairoff10[4] ).M() ) / 2 ), scale )
			if pairoff11[0]: 
				deltaR_Pairing11.Fill( pairoff11[5] )
				massAve_Pairing11.Fill( ( ( ( pairoff11[1] + pairoff11[2] ).M() + ( pairoff11[3] + pairoff11[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 50 ):
					deltaR_Pairing11_Pt50.Fill( pairoff11[5] )
					massAve_Pairing11_Pt50.Fill( ( ( ( pairoff11[1] + pairoff11[2] ).M() + ( pairoff11[3] + pairoff11[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 60 ):
					deltaR_Pairing11_Pt60.Fill( pairoff11[5] )
					massAve_Pairing11_Pt60.Fill( ( ( ( pairoff11[1] + pairoff11[2] ).M() + ( pairoff11[3] + pairoff11[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 70 ):
					deltaR_Pairing11_Pt70.Fill( pairoff11[5] )
					massAve_Pairing11_Pt70.Fill( ( ( ( pairoff11[1] + pairoff11[2] ).M() + ( pairoff11[3] + pairoff11[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 80 ):
					deltaR_Pairing11_Pt80.Fill( pairoff11[5] )
					massAve_Pairing11_Pt80.Fill( ( ( ( pairoff11[1] + pairoff11[2] ).M() + ( pairoff11[3] + pairoff11[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 100 ):
					deltaR_Pairing11_Pt100.Fill( pairoff11[5] )
					massAve_Pairing11_Pt100.Fill( ( ( ( pairoff11[1] + pairoff11[2] ).M() + ( pairoff11[3] + pairoff11[4] ).M() ) / 2 ), scale )
			if pairoff12[0]: 
				deltaR_Pairing12.Fill( pairoff12[5] )
				massAve_Pairing12.Fill( ( ( ( pairoff12[1] + pairoff12[2] ).M() + ( pairoff12[3] + pairoff12[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 50 ):
					deltaR_Pairing12_Pt50.Fill( pairoff12[5] )
					massAve_Pairing12_Pt50.Fill( ( ( ( pairoff12[1] + pairoff12[2] ).M() + ( pairoff12[3] + pairoff12[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 60 ):
					deltaR_Pairing12_Pt60.Fill( pairoff12[5] )
					massAve_Pairing12_Pt60.Fill( ( ( ( pairoff12[1] + pairoff12[2] ).M() + ( pairoff12[3] + pairoff12[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 70 ):
					deltaR_Pairing12_Pt70.Fill( pairoff12[5] )
					massAve_Pairing12_Pt70.Fill( ( ( ( pairoff12[1] + pairoff12[2] ).M() + ( pairoff12[3] + pairoff12[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 80 ):
					deltaR_Pairing12_Pt80.Fill( pairoff12[5] )
					massAve_Pairing12_Pt80.Fill( ( ( ( pairoff12[1] + pairoff12[2] ).M() + ( pairoff12[3] + pairoff12[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 100 ):
					deltaR_Pairing12_Pt100.Fill( pairoff12[5] )
					massAve_Pairing12_Pt100.Fill( ( ( ( pairoff12[1] + pairoff12[2] ).M() + ( pairoff12[3] + pairoff12[4] ).M() ) / 2 ), scale )
			if pairoff13[0]: 
				deltaR_Pairing13.Fill( pairoff13[5] )
				massAve_Pairing13.Fill( ( ( ( pairoff13[1] + pairoff13[2] ).M() + ( pairoff13[3] + pairoff13[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 50 ):
					deltaR_Pairing13_Pt50.Fill( pairoff13[5] )
					massAve_Pairing13_Pt50.Fill( ( ( ( pairoff13[1] + pairoff13[2] ).M() + ( pairoff13[3] + pairoff13[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 60 ):
					deltaR_Pairing13_Pt60.Fill( pairoff13[5] )
					massAve_Pairing13_Pt60.Fill( ( ( ( pairoff13[1] + pairoff13[2] ).M() + ( pairoff13[3] + pairoff13[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 70 ):
					deltaR_Pairing13_Pt70.Fill( pairoff13[5] )
					massAve_Pairing13_Pt70.Fill( ( ( ( pairoff13[1] + pairoff13[2] ).M() + ( pairoff13[3] + pairoff13[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 80 ):
					deltaR_Pairing13_Pt80.Fill( pairoff13[5] )
					massAve_Pairing13_Pt80.Fill( ( ( ( pairoff13[1] + pairoff13[2] ).M() + ( pairoff13[3] + pairoff13[4] ).M() ) / 2 ), scale )
				if ( jetsPt[3] > 100 ):
					deltaR_Pairing13_Pt100.Fill( pairoff13[5] )
					massAve_Pairing13_Pt100.Fill( ( ( ( pairoff13[1] + pairoff13[2] ).M() + ( pairoff13[3] + pairoff13[4] ).M() ) / 2 ), scale )

		'''
=======
			
		if pairoff08[0]: deltaR_Pairing08.Fill( pairoff08[5] )
		if pairoff09[0]: deltaR_Pairing09.Fill( pairoff09[5] )
		if pairoff10[0]: deltaR_Pairing10.Fill( pairoff10[5] )
		if pairoff11[0]: deltaR_Pairing11.Fill( pairoff11[5] )
		if pairoff12[0]: deltaR_Pairing12.Fill( pairoff12[5] )

>>>>>>> 1ed1f13e9a39e2d9412a067d05462ef0c0cedbeb
		if pairoff08[0]:

			deltaR = pairoff08[5] 
			deltaR_Pairing.Fill( deltaR )
			dijet1 = pairoff08[1] + pairoff08[2]
			dijet2 = pairoff08[3] + pairoff08[4]
			massPairing = ( dijet1.M() - dijet2.M() ) / ( dijet1.M() + dijet2.M() )
			massPairing_Pairing.Fill( massPairing )
			deltaEta = abs( dijet1.Eta() - dijet2.Eta() )
			deltaEtaDijet_Pairing.Fill( deltaEta )
			massAve = ( dijet1.M() + dijet2.M() ) / 2
			massAve_Pairing.Fill( massAve, scale )

			deltaEtaDijet1_Pairing.Fill( abs( pairoff08[1].Eta() - pairoff08[2].Eta() ) )	
			deltaEtaDijet2_Pairing.Fill( abs( pairoff08[3].Eta() - pairoff08[4].Eta() ) )	
			deltaEtaBest = ( abs( pairoff08[1].Eta() - pairoff08[2].Eta() ) + abs( pairoff08[3].Eta() - pairoff08[4].Eta()  ) ) / 2
			deltaEtaBest_Pairing.Fill( deltaEtaBest, scale )

			deltaPhiDijet_Pairing.Fill( pairoff08[1].DeltaPhi( pairoff08[2] ) )	
			deltaPhiDijet_Pairing.Fill( pairoff08[3].DeltaPhi( pairoff08[4] ) )	
			deltaPhiBest = ( pairoff08[1].DeltaPhi( pairoff08[2] ) + pairoff08[3].DeltaPhi( pairoff08[4] ) ) / 2
			deltaPhiBest_Pairing.Fill( deltaPhiBest, scale )

			deltaRDijet_Pairing.Fill( pairoff08[1].DeltaR( pairoff08[2] ) )	
			deltaRDijet_Pairing.Fill( pairoff08[3].DeltaR( pairoff08[4] ) )	
			deltaRBest = ( pairoff08[1].DeltaR( pairoff08[2] ) + pairoff08[3].DeltaR( pairoff08[4] ) ) / 2
			deltaRBest_Pairing.Fill( deltaRBest, scale )

			tmpCM1 = pairoff08[1] + pairoff08[2]
			tmpJ1 = pairoff08[1]
			tmpJ2 = pairoff08[2]
			tmpJ1.Boost( -tmpCM1.BoostVector() )
			tmpJ2.Boost( -tmpCM1.BoostVector() )
			tmpV1 = TVector3( tmpJ1.X(), tmpJ1.Y(), tmpJ1.Z() )
			tmpV2 = TVector3( tmpJ2.X(), tmpJ2.Y(), tmpJ2.Z() )
			#cosThetaStar1 = abs( ( ( pairoff08[1].Px() * pairoff08[2].Px() ) + ( pairoff08[1].Py() * pairoff08[2].Py() ) + ( pairoff08[1].Pz() * pairoff08[2].Pz() ) )  / ( pairoff08[1].E() * pairoff08[2].E() ) )
			cosThetaStar1 = abs( tmpV1.CosTheta() )
			cosThetaStar1_Pairing.Fill( cosThetaStar1, scale )

			tmpCM2 = pairoff08[3] + pairoff08[4]
			tmpJ3 = pairoff08[3]
			tmpJ4 = pairoff08[4]
			tmpJ3.Boost( -tmpCM2.BoostVector() )
			tmpJ4.Boost( -tmpCM2.BoostVector() )
			tmpV3 = TVector3( tmpJ3.X(), tmpJ3.Y(), tmpJ3.Z() )
			tmpV4 = TVector3( tmpJ4.X(), tmpJ4.Y(), tmpJ4.Z() )
			cosThetaStar2 = abs( tmpV3.CosTheta() )
			#cosThetaStar2 = abs( ( ( pairoff08[3].Px() * pairoff08[4].Px() ) + ( pairoff08[3].Py() * pairoff08[4].Py() ) + ( pairoff08[3].Pz() * pairoff08[4].Pz() ) )  / ( pairoff08[3].E() * pairoff08[4].E() ) )
			cosThetaStar2_Pairing.Fill( cosThetaStar2, scale )

			if ( deltaRBest < 2 ):
				massAve_DeltaRBest.Fill( massAve, scale )
			if ( deltaR < 1.5 ):
				massAve_DeltaR.Fill( massAve, scale )
<<<<<<< HEAD
				if ( ( cosThetaStar1 < 0.7 ) and ( cosThetaStar2 < 0.7 ) ):
					massAve_DeltaRCosTheta.Fill( massAve, scale )
					if ( deltaEta < 1 ):
						massAve_DeltaRCosThetaDeltaEta.Fill( massAve, scale )
						if ( massPairing < 0.1 ):
							massAve_DeltaRCosThetaDeltaEtaMassPar.Fill( massAve, scale )
			if ( deltaEta < 1 ):
				massAve_DeltaEta.Fill( massAve, scale )
			if ( massPairing < 0.1 ):
				massAve_MassPar.Fill( massAve, scale )
			if ( ( cosThetaStar1 < 0.7 ) and ( cosThetaStar2 < 0.7 ) ):
				massAve_CosTheta.Fill( massAve, scale )
			
			if jetsPtCut:
				if (HT > 800) and ( ( delta1 > 300 ) and ( delta2 > 300 ) ):
					massAve_Delta_cutJetPt.Fill( massAve, scale )
					if ( deltaEta < 1 ):
						massAve_DeltaDeltaEta_cutJetPt.Fill( massAve, scale )
						if ( massPairing < 0.1 ):
							massAve_DeltaMassPar_cutJetPt.Fill( massAve, scale )
							#if ( massAve > 900 ): print 'MassAve ', massAve,  'Entry ', Run, ':', Lumi, ':', NumEvent
			else:
				if (HT > 800) and ( ( delta1 > 300 ) and ( delta2 > 300 ) ):
					massAve_Delta.Fill( massAve, scale )
					if ( deltaEta < 1 ):
						massAve_DeltaDeltaEta.Fill( massAve, scale )
						if ( massPairing < 0.1 ):
							massAve_DeltaMassPar.Fill( massAve, scale )
		'''
=======
				if ( deltaEta < 1 ):
					massAve_DeltaEta.Fill( massAve, scale )
					if ( massPairing < 0.1 ):
						massAve_MassPar.Fill( massAve, scale )
						if ( deltaRBest < 2 ):
							massAve_EtaMassParDeltaR.Fill( massAve, scale )
			if ( ( delta1 < 300 ) and ( delta2 < 300 ) ):
				massAve_Delta.Fill( massAve, scale )
				if ( deltaR < 1.5 ):
					massAve_DeltaDeltaR.Fill( massAve, scale )
					if ( deltaEta < 1 ):
						massAve_DeltaDeltaEta.Fill( massAve, scale )
						if ( massPairing < 0.1 ):
							massAve_DeltaMassPar.Fill( massAve, scale )
							if ( deltaRBest < 2 ):
								massAve_DeltaEtaMassParDeltaR.Fill( massAve, scale )

			if ( ( cosThetaStar1 < 0.4 ) and ( cosThetaStar2 < 0.4 ) ):
				massAve_CosTheta.Fill( massAve, scale )
				if ( deltaR < 1.5 ):
					massAve_CosThetaDeltaR.Fill( massAve, scale )
					if ( deltaEta < 1 ):
						massAve_CosThetaDeltaEta.Fill( massAve, scale )
						if ( massPairing < 0.1 ):
							massAve_CosThetaMassPar.Fill( massAve, scale )
							if ( deltaRBest < 2 ):
								massAve_CosThetaEtaMassParDeltaR.Fill( massAve, scale )
>>>>>>> 1ed1f13e9a39e2d9412a067d05462ef0c0cedbeb



	outputFile.Write()

	##### Closing
	print 'Writing output file: '+ outputFileName
	outputFile.Close()

	###### Extra: send prints to file
	#if couts == False: 
	#	sys.stdout = outfileStdOut
	#	f.close()
	#########################


#################################################################################
if __name__ == '__main__':

	usage = 'usage: %prog [options]'
	
	parser = argparse.ArgumentParser()
	parser.add_argument( '-m', '--mass', action='store', type=int, dest='mass', default=350, help='Mass of the Stop' )
	parser.add_argument( '-p', '--pileup', action='store',  dest='pileup', default='Asympt25ns', help='Pileup' )
	parser.add_argument( '-d', '--debug', action='store_true', dest='couts', default=False, help='True print couts in screen, False print in a file' )
	parser.add_argument( '-s', '--sample', action='store',   dest='samples', default='RPV', help='Type of sample' )

	try:
		args = parser.parse_args()
	except:
		parser.print_help()
		sys.exit(0)

	mass = args.mass
	PU = args.pileup
	couts = args.couts
	samples = args.samples

	if 'RPV' in samples: 
<<<<<<< HEAD
		inputFileName = 'Rootfiles/RUNAnalysis_RPVSt'+str(mass)+'tojj_RunIISpring15MiniAODv2-74X_'+PU+'_v08_v04.root'
	elif 'Data' in samples: 
		inputFileName = 'Rootfiles/RUNAnalysis_JetHTRun2015D-All_v08_v04.root'
	elif 'Bkg' in samples: 
		inputFileName = 'Rootfiles/RUNAnalysis_WJetsToQQ_HT-600ToInf_RunIISpring15DR74_Asympt25ns_v03_v01.root'
		inputFileName = 'Rootfiles/RUNAnalysis_ZJetsToQQ_HT600ToInf_RunIISpring15DR74_Asympt25ns_v03_v01.root'
		inputFileName = 'Rootfiles/RUNAnalysis_TTJets_RunIISpring15DR74_Asympt25ns_v03_v01.root'
=======
		inputFileName = 'Rootfiles/RUNAnalysis_RPVSt'+str(mass)+'tojj_RunIISpring15MiniAODv2-74X_'+PU+'_v08_v02.root'
		myAnalyzer( inputFileName, couts)
	elif 'Data' in samples: 
		inputFileName = 'Rootfiles/RUNAnalysis_JetHTRun2015D-PromptReco-v4_v08_v01.root'
		myAnalyzer( inputFileName, couts)
	elif 'Bkg' in samples: 
		inputFileName = 'Rootfiles/RUNAnalysis_WJetsToQQ_HT-600ToInf_RunIISpring15DR74_Asympt25ns_v03_v01.root'
		myAnalyzer( inputFileName, couts)
		inputFileName = 'Rootfiles/RUNAnalysis_ZJetsToQQ_HT600ToInf_RunIISpring15DR74_Asympt25ns_v03_v01.root'
		myAnalyzer( inputFileName, couts)
		inputFileName = 'Rootfiles/RUNAnalysis_TTJets_RunIISpring15DR74_Asympt25ns_v03_v01.root'
		myAnalyzer( inputFileName, couts)
>>>>>>> 1ed1f13e9a39e2d9412a067d05462ef0c0cedbeb
	else: 
		#for qcdBin in [ '170to300', '300to470', '470to600', '600to800', '800to1000', '1000to1400', '1400to1800', '1800to2400', '2400to3200', '3200toInf' ]: 
		#	inputFileName = 'Rootfiles//RUNAnalysis_QCD_Pt_'+qcdBin+'_RunIISpring15MiniAODv2-74X_'+PU+'_v08_v02.root'
		#	myAnalyzer( inputFileName, couts )
<<<<<<< HEAD
		inputFileName = 'Rootfiles/RUNAnalysis_QCDPtAll_RunIISpring15MiniAODv2-74X_Asympt25ns_v08_v04.root'
	p = Process( target=myAnalyzer, args=( inputFileName, couts ) )
	p.start()
	p.join()
=======
		inputFileName = 'Rootfiles/RUNAnalysis_QCDPtAll_RunIISpring15MiniAODv2-74X_Asympt25ns_v08_v02.root'
		myAnalyzer( inputFileName, couts )
>>>>>>> 1ed1f13e9a39e2d9412a067d05462ef0c0cedbeb

