//////////////////////////////////////////////////////////
//   This class has been generated by TFile::MakeProject
//     (Fri Feb 24 17:58:52 2023 by ROOT version 6.14/06)
//      from the StreamerInfo in file ../run-edep-sim/output/MiniRun1_1E19_RHC_nu/EDEPSIM/g4numiv6_minervame_me000z-200i_0_0001.000.EDEPSIM.root
//////////////////////////////////////////////////////////


#ifndef TG4HitSegment_h
#define TG4HitSegment_h
class TG4HitSegment;

#include "Rtypes.h"
#include "TObject.h"
#include "Riostream.h"
#include <vector>
#include "TLorentzVector.h"

class TG4HitSegment : public TObject {

public:
// Nested classes declaration.

public:
// Data Members.
   vector<int> Contrib;     //
   int         PrimaryId;    //
   float       EnergyDeposit;    //
   float       SecondaryDeposit;    //
   float       TrackLength;         //
   TLorentzVector Start;               //
   TLorentzVector Stop;                //

   TG4HitSegment();
   TG4HitSegment(const TG4HitSegment & );
   virtual ~TG4HitSegment();

   ClassDef(TG4HitSegment,2); // Generated by MakeProject.
};
#endif
