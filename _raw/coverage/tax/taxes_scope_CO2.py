#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 07:54:30 2021

@author: gd
"""
    
def coverage():    
    # Argentina
    
    ## Jurisdiction
    
    arg_tax_jur_I = ["Argentina"]

    ## Sectors
    
    arg_tax_ipcc_I = ["1A1A1", "1A1A2", "1A1A3", "1A1B", "1A1C", "1A2A",
                      "1A2B", "1A2C", "1A2D", "1A2E", "1A2F", "1A2G", "1A2H",
                      "1A2I", "1A2J", "1A2K", "1A2L", "1A2M", "1A3A2",
                      "1A3B", "1A3C", "1A3D2", "1A3E1", "1A4A", "1A4B",
                      "1A4C1", "1A4C2", "1A4C3", "1A5A", "1A5B", "1A5C"]
    
    ## Fuels
    
    arg_tax_fuel_I = ["Oil"]
    arg_tax_fuel_II = ["Oil", "Coal/peat"]

    ## Coverage dictionaries
    arg_tax_jur_coverage = {2018:arg_tax_jur_I, 2019:arg_tax_jur_I, 
                            2020:arg_tax_jur_I, 2021:arg_tax_jur_I}
    
    arg_tax_ipcc_coverage = {2018:arg_tax_ipcc_I, 2019:arg_tax_ipcc_I, 
                             2020:arg_tax_ipcc_I, 2021:arg_tax_ipcc_I}     

    arg_tax_fuel_coverage = {2018:arg_tax_fuel_I, 2019:arg_tax_fuel_II, 
                             2020:arg_tax_fuel_II, 2021:arg_tax_fuel_II} 
    
    ## Sources dictionary
    
    arg_tax_coverage_sources = {2018:"leg(AR[2017),report(WB[2018]])", 
                                2019:"leg(AR[2017),report(WB[2018]])", 
                                2020:"leg(AR[2017),report(WB[2018]])",
                                2021:"leg(AR[2017),report(WB[2018]])"}

    
    #----------------------------------------------------------------------------
    
    # Australia (Carbon price mechanism)
    
    ## Jurisdiction
    
    aus_tax_jur_I = ["Australia"]

    ## Sectors
    
    aus_tax_ipcc_I = ["1A1A1", "1A1A2", "1A1A3", "1A2A", "1A2B", "1A2C",
                      "1A2D", "1A2E", "1A2F", "1A2G", "1A2H", "1A2I", "1A2J",
                      "1A2K", "1A2L", "1A2M"]
    
    ## Fuels
    
    aus_tax_fuel_I = ["Oil", "Natural gas", "Coal/peat"]

    ## Coverage dictionaries
    aus_tax_jur_coverage = {2012:aus_tax_jur_I, 2013:aus_tax_jur_I, 
                            2014:aus_tax_jur_I}
    
    aus_tax_ipcc_coverage = {2012:aus_tax_ipcc_I, 2013:aus_tax_ipcc_I, 
                             2014:aus_tax_ipcc_I}     

    aus_tax_fuel_coverage = {2012:aus_tax_fuel_I, 2013:aus_tax_fuel_I, 
                             2014:aus_tax_fuel_I} 
    
    ## Sources dictionary
    
    aus_tax_coverage_sources = {2012:"leg(AU-NGER[2011]),db(AU-CER-LEPID[2012])", 
                                2013:"leg(AU-NGER[2011]),db(AU-CER-LEPID[2013])", 
                                2014:"leg(AU-NGER[2011]),db(AU-CER-LEPID[2013])"}

    
    #----------------------------------------------------------------------------
   
    # Chile
    
    ## Jurisdiction
    
    chl_tax_jur_I = ["Chile"]

    ## Sectors
    
    chl_tax_ipcc_I = ["1A1A1", "1A2A",
                      "1A2B", "1A2C", "1A2D", "1A2E", "1A2F", "1A2G", "1A2H",
                      "1A2I", "1A2J", "1A2K", "1A2L", "1A2M"]
    
    ## Fuels
    
    chl_tax_fuel_I = ["Oil", "Coal/peat", "Natural gas"]

    ## Coverage dictionaries
    chl_tax_jur_coverage = {2017:chl_tax_jur_I, 2018:chl_tax_jur_I, 
                            2019:chl_tax_jur_I, 2020:chl_tax_jur_I, 
                            2021:chl_tax_jur_I}
    
    chl_tax_ipcc_coverage = {2017:chl_tax_ipcc_I, 2018:chl_tax_ipcc_I, 
                             2019:chl_tax_ipcc_I, 2020:chl_tax_ipcc_I, 
                             2021:chl_tax_ipcc_I}     

    chl_tax_fuel_coverage = {2017:chl_tax_fuel_I, 2018:chl_tax_fuel_I, 
                             2019:chl_tax_fuel_I, 2020:chl_tax_fuel_I, 
                             2021:chl_tax_fuel_I} 

    ## Sources dictionary
    
    chl_tax_coverage_sources = {2017:"report(WB[2017])", 2018:"report(WB[2018])", 
                                2019:"report(WB[2018])", 2020:"report(WB[2018])",
                                2021:"report(WB[2021])"}

    #----------------------------------------------------------------------------
    
    # British Columbia
    
    ## Jurisdiction
    
    can_bc_tax_jur_I = ["British Columbia"]

    ## Sectors
    
    # initial coverage
    can_bc_tax_ipcc_I = ["1A1A1", "1A1A2", "1A1A3", "1A1B", "1A1C", "1A2A", "1A2B",
                     "1A2C", "1A2D", "1A2E", "1A2F", "1A2G", "1A2H", "1A2I",
                     "1A2J", "1A2K", "1A2L", "1A2M", "1A3A2", "1A3B", "1A3C",
                     "1A3D2", "1A3E1", "1A4A", "1A4B", "1A4C1",
                     "1A4C2", "1A4C3", "1A5A", "1A5B", "1A5C"]

    ## Fuels
    
    can_bc_tax_fuel_I = ["Oil", "Natural gas", "Coal/peat"]
    
    
    ## Greenhouse gases
    
    can_bc_tax_gas_I = ["CO2", "CH4", "N2O"]
    
    

    ## Coverage dictionaries
    
    can_bc_tax_jur_coverage = {2011:can_bc_tax_jur_I,
                            2012:can_bc_tax_jur_I, 2013:can_bc_tax_jur_I,
                            2014:can_bc_tax_jur_I, 2015:can_bc_tax_jur_I,
                            2016:can_bc_tax_jur_I, 2017:can_bc_tax_jur_I,
                            2018:can_bc_tax_jur_I, 2019:can_bc_tax_jur_I, 
                            2020:can_bc_tax_jur_I}
    
    can_bc_tax_ipcc_coverage = {2011:can_bc_tax_ipcc_I,
                            2012:can_bc_tax_ipcc_I, 2013:can_bc_tax_ipcc_I,
                            2014:can_bc_tax_ipcc_I, 2015:can_bc_tax_ipcc_I,
                            2016:can_bc_tax_ipcc_I, 2017:can_bc_tax_ipcc_I,
                            2018:can_bc_tax_ipcc_I, 2019:can_bc_tax_ipcc_I, 
                            2020:can_bc_tax_ipcc_I}
    
    can_bc_tax_fuel_coverage = {2011:can_bc_tax_fuel_I,
                            2012:can_bc_tax_fuel_I, 2013:can_bc_tax_fuel_I,
                            2014:can_bc_tax_fuel_I, 2015:can_bc_tax_fuel_I,
                            2016:can_bc_tax_fuel_I, 2017:can_bc_tax_fuel_I,
                            2018:can_bc_tax_fuel_I, 2019:can_bc_tax_fuel_I, 
                            2020:can_bc_tax_fuel_I}
    
    ## Sources dictionary
    
    can_bc_tax_coverage_sources = {2011:"leg(BC-CTA[2008]), gvt(BCGOV[2021])", 
                                   2012:"leg(BC-CTA[2008]), gvt(BCGOV[2021])",
                                   2013:"leg(BC-CTA[2008]), gvt(BCGOV[2021])", 
                                   2014:"leg(BC-CTA[2008]), gvt(BCGOV[2021])", 
                                   2015:"leg(BC-CTA[2008]), gvt(BCGOV[2021])", 
                                   2016:"leg(BC-CTA[2008]), gvt(BCGOV[2021])",
                                   2017:"leg(BC-CTA[2008]), gvt(BCGOV[2021])", 
                                   2018:"leg(BC-CTA[2008]), gvt(BCGOV[2021])", 
                                   2019:"leg(BC-CTA[2008]), gvt(BCGOV[2021])", 
                                   2020:"leg(BC-CTA[2008]), gvt(BCGOV[2021])",
                                   2021:"leg(BC-CTA[2008]), gvt(BCGOV[2021])"}

    #----------------------------------------------------------------------------

    # Colombia
    
    ## Jurisdiction
    
    col_tax_jur_I = ["Colombia"]

    ## Sectors
    
    col_tax_ipcc_I = ["1A1A1", "1A1A2", "1A1A3", "1A2A",
                      "1A2B", "1A2C", "1A2D", "1A2E", "1A2F", "1A2G", "1A2H",
                      "1A2I", "1A2J", "1A2K", "1A2L", "1A2M"]
    
    ## Fuels
    
    col_tax_fuel_I = ["Oil", "Natural gas"]

    ## Coverage dictionaries
    
    col_tax_jur_coverage = {2017:col_tax_jur_I, 2018:col_tax_jur_I, 
                            2019:col_tax_jur_I, 2020:col_tax_jur_I, 
                            2021:col_tax_jur_I}
    
    col_tax_ipcc_coverage = {2017:col_tax_ipcc_I, 2018:col_tax_ipcc_I, 
                             2019:col_tax_ipcc_I, 2020:col_tax_ipcc_I, 
                             2021:col_tax_ipcc_I}     

    col_tax_fuel_coverage = {2017:col_tax_fuel_I, 2018:col_tax_fuel_I, 
                             2019:col_tax_fuel_I, 2020:col_tax_fuel_I, 
                             2021:col_tax_fuel_I}     

    ## Sources dictionary
    
    col_tax_coverage_sources = {2017:"report(OECD-TEU-COL[2019]),gvt(COL-DIAN[2017])", 
                                2018:"report(OECD-TEU-COL[2019]),gvt(COL-DIAN[2017])", 
                                2019:"report(OECD-TEU-COL[2019]),gvt(COL-DIAN[2017])", 
                                2020:"report(OECD-TEU-COL[2019]),gvt(COL-DIAN[2017])",
                                2021:"report(OECD-TEU-COL[2019]),gvt(COL-DIAN[2017])"}

    #----------------------------------------------------------------------------

    # Denmark
    
    ## Jurisdictions    
    
    dnk_tax_jur_I = ["Denmark"]
    
    ## Sectors
    dnk_tax_ipcc_I = ["1A1A1", "1A1A3", "1A1B", "1A1C", "1A2A", "1A2B", "1A2C",
                        "1A2D", "1A2E", "1A2F", "1A2G", "1A2H", "1A2I", "1A2J",
                        "1A2K", "1A2L", "1A2M", "1A3B", "1A4A", "1A4B",
                        "1A4C1"]

    dnk_tax_ipcc_II = ["1A1A3", "1A1B", "1A1C", "1A3B", "1A4A", "1A4B",
                        "1A4C1"]        
    
    ## Fuels

    dnk_tax_I_fuel_I = ["Oil", "Coal/peat", "Natural gas"]      
    
    ## Coverage dictionaries

    dnk_tax_jur_coverage = {1992:dnk_tax_jur_I,
                              1993:dnk_tax_jur_I, 1994:dnk_tax_jur_I,
                              1995:dnk_tax_jur_I, 1996:dnk_tax_jur_I,
                              1997:dnk_tax_jur_I, 1998:dnk_tax_jur_I,
                              1999:dnk_tax_jur_I, 2000:dnk_tax_jur_I,
                              2001:dnk_tax_jur_I, 2002:dnk_tax_jur_I,
                              2003:dnk_tax_jur_I, 2004:dnk_tax_jur_I,
                              2005:dnk_tax_jur_I, 2006:dnk_tax_jur_I,
                              2007:dnk_tax_jur_I, 2008:dnk_tax_jur_I,
                              2009:dnk_tax_jur_I, 2010:dnk_tax_jur_I,
                              2011:dnk_tax_jur_I, 2012:dnk_tax_jur_I,
                              2013:dnk_tax_jur_I, 2014:dnk_tax_jur_I,
                              2015:dnk_tax_jur_I, 2016:dnk_tax_jur_I,
                              2017:dnk_tax_jur_I, 2018:dnk_tax_jur_I,
                              2019:dnk_tax_jur_I, 2020:dnk_tax_jur_I,
                              2021:dnk_tax_jur_I}

    dnk_tax_ipcc_coverage = {1992:dnk_tax_ipcc_I,
                              1993:dnk_tax_ipcc_I, 1994:dnk_tax_ipcc_I,
                              1995:dnk_tax_ipcc_I, 1996:dnk_tax_ipcc_I,
                              1997:dnk_tax_ipcc_I, 1998:dnk_tax_ipcc_I,
                              1999:dnk_tax_ipcc_I, 2000:dnk_tax_ipcc_I,
                              2001:dnk_tax_ipcc_I, 2002:dnk_tax_ipcc_I,
                              2003:dnk_tax_ipcc_I, 2004:dnk_tax_ipcc_I,
                              2005:dnk_tax_ipcc_II, 2006:dnk_tax_ipcc_II,
                              2007:dnk_tax_ipcc_II, 2008:dnk_tax_ipcc_II,
                              2009:dnk_tax_ipcc_II, 2010:dnk_tax_ipcc_II,
                              2011:dnk_tax_ipcc_II, 2012:dnk_tax_ipcc_II,
                              2013:dnk_tax_ipcc_II, 2014:dnk_tax_ipcc_II,
                              2015:dnk_tax_ipcc_II, 2016:dnk_tax_ipcc_II,
                              2017:dnk_tax_ipcc_II, 2018:dnk_tax_ipcc_II,
                              2019:dnk_tax_ipcc_II, 2020:dnk_tax_ipcc_II,
                              2021:dnk_tax_ipcc_II}
    
    dnk_tax_fuel_coverage = {1992:dnk_tax_I_fuel_I,
                              1993:dnk_tax_I_fuel_I, 1994:dnk_tax_I_fuel_I,
                              1995:dnk_tax_I_fuel_I, 1996:dnk_tax_I_fuel_I,
                              1997:dnk_tax_I_fuel_I, 1998:dnk_tax_I_fuel_I,
                              1999:dnk_tax_I_fuel_I, 2000:dnk_tax_I_fuel_I,
                              2001:dnk_tax_I_fuel_I, 2002:dnk_tax_I_fuel_I,
                              2003:dnk_tax_I_fuel_I, 2004:dnk_tax_I_fuel_I,
                              2005:dnk_tax_I_fuel_I, 2006:dnk_tax_I_fuel_I,
                              2007:dnk_tax_I_fuel_I, 2008:dnk_tax_I_fuel_I,
                              2009:dnk_tax_I_fuel_I, 2010:dnk_tax_I_fuel_I,
                              2011:dnk_tax_I_fuel_I, 2012:dnk_tax_I_fuel_I,
                              2013:dnk_tax_I_fuel_I, 2014:dnk_tax_I_fuel_I,
                              2015:dnk_tax_I_fuel_I, 2016:dnk_tax_I_fuel_I,
                              2017:dnk_tax_I_fuel_I, 2018:dnk_tax_I_fuel_I,
                              2019:dnk_tax_I_fuel_I, 2020:dnk_tax_I_fuel_I,
                              2021:dnk_tax_I_fuel_I}
    
    ## Sources dictionary
    
    dnk_tax_coverage_sources = {1992:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])",
                                1993:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])", 
                                1994:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])",
                                1995:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])", 
                                1996:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])",
                                1997:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])", 
                                1998:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])",
                                1999:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])", 
                                2000:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])",
                                2001:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])", 
                                2002:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])",
                                2003:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])", 
                                2004:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])",
                                2005:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])", 
                                2006:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])",
                                2007:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])", 
                                2008:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])",
                                2009:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])", 
                                2010:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])",
                                2011:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])", 
                                2012:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])",
                                2013:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])", 
                                2014:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])",
                                2015:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])", 
                                2016:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])",
                                2017:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])", 
                                2018:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])",
                                2019:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])", 
                                2020:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])",
                                2021:"journal(WIE[2005]), report(NBER[2009], NC-EIN[2006], IEA-DK[2002])"}

    #----------------------------------------------------------------------------

    # Estonia
    
    ## Jurisdiction
    
    est_tax_jur_I = ["Estonia"]

    ## Sectors
    
    # initial coverage
    est_tax_ipcc_I = ["1A1A1", "1A1A2", "1A1A3", 
                      "1A2A", "1A2B", "1A2C", "1A2D", "1A2E", "1A2F", "1A2G", 
                      "1A2H", "1A2I", "1A2J", "1A2K", "1A2L", "1A2M"]

    ## Fuels
    
    est_tax_fuel_I = ["Oil", "Natural gas", "Coal/peat"]

    ## Coverage dictionaries
    
    est_tax_jur_coverage = {2000:est_tax_jur_I, 2001:est_tax_jur_I,
                            2002:est_tax_jur_I, 2003:est_tax_jur_I,
                            2004:est_tax_jur_I, 2005:est_tax_jur_I,
                            2006:est_tax_jur_I, 2007:est_tax_jur_I,
                            2008:est_tax_jur_I, 2009:est_tax_jur_I,
                            2010:est_tax_jur_I, 2011:est_tax_jur_I,
                            2012:est_tax_jur_I, 2013:est_tax_jur_I,
                            2014:est_tax_jur_I, 2015:est_tax_jur_I,
                            2016:est_tax_jur_I, 2017:est_tax_jur_I,
                            2018:est_tax_jur_I, 2019:est_tax_jur_I, 
                            2020:est_tax_jur_I}
    
    est_tax_ipcc_coverage = {2000:est_tax_ipcc_I, 2001:est_tax_ipcc_I,
                            2002:est_tax_ipcc_I, 2003:est_tax_ipcc_I,
                            2004:est_tax_ipcc_I, 2005:est_tax_ipcc_I,
                            2006:est_tax_ipcc_I, 2007:est_tax_ipcc_I,
                            2008:est_tax_ipcc_I, 2009:est_tax_ipcc_I,
                            2010:est_tax_ipcc_I, 2011:est_tax_ipcc_I,
                            2012:est_tax_ipcc_I, 2013:est_tax_ipcc_I,
                            2014:est_tax_ipcc_I, 2015:est_tax_ipcc_I,
                            2016:est_tax_ipcc_I, 2017:est_tax_ipcc_I,
                            2018:est_tax_ipcc_I, 2019:est_tax_ipcc_I, 
                            2020:est_tax_ipcc_I}
    
    est_tax_fuel_coverage = {2000:est_tax_fuel_I, 2001:est_tax_fuel_I,
                            2002:est_tax_fuel_I, 2003:est_tax_fuel_I,
                            2004:est_tax_fuel_I, 2005:est_tax_fuel_I,
                            2006:est_tax_fuel_I, 2007:est_tax_fuel_I,
                            2008:est_tax_fuel_I, 2009:est_tax_fuel_I,
                            2010:est_tax_fuel_I, 2011:est_tax_fuel_I,
                            2012:est_tax_fuel_I, 2013:est_tax_fuel_I,
                            2014:est_tax_fuel_I, 2015:est_tax_fuel_I,
                            2016:est_tax_fuel_I, 2017:est_tax_fuel_I,
                            2018:est_tax_fuel_I, 2019:est_tax_fuel_I, 
                            2020:est_tax_fuel_I}

    ## Sources dictionary
    
    est_tax_coverage_sources = {2000:"",
                                2001:"", 2002:"", 2003:"",
                                2004:"", 2005:"report(EST-SE[2009]) ", 
                                2006:"report(EST-SE[2009])",
                                2007:"report(EST-SE[2009])", 
                                2008:"report(EST-SE[2009])", 
                                2009:"report(EST-SE[2009])",
                                2010:"report(EST-SE[2009])", 
                                2011:"leg(EST-ECA[2005])", 
                                2012:"leg(EST-ECA[2005])",
                                2013:"leg(EST-ECA[2005])", 
                                2014:"leg(EST-ECA[2005])", 
                                2015:"leg(EST-ECA[2005])", 
                                2016:"leg(EST-ECA[2005]), report(OECD[2019]), db(WCPD[2020])",
                                2017:"leg(EST-ECA[2005]), report(OECD[2019]), db(WCPD[2020])", 
                                2018:"leg(EST-ECA[2005]), report(OECD[2019]), db(WCPD[2020])", 
                                2019:"leg(EST-ECA[2005]), report(OECD[2019]), db(WCPD[2020])", 
                                2020:"leg(EST-ECA[2005]), report(OECD[2019]), db(WCPD[2020])",
                                2021:""}

    #----------------------------------------------------------------------------

    # Finland
    
    ## Jurisdictions    
    
    fin_tax_jur_I = ["Finland"]
    
    ## Sectors
    fin_tax_ipcc_I = ["1A1B", "1A1C", "1A2A", "1A2B", "1A2C",
                      "1A2D", "1A2E", "1A2F", "1A2G", "1A2H", "1A2I", "1A2J",
                      "1A2K", "1A2L", "1A2M", "1A3A2", 
                      "1A4A", "1A4B", "1A4C1", "1A4C2"]

    fin_tax_ipcc_II = ["1A1B", "1A1C", "1A2A", "1A2B", "1A2C",
                      "1A2D", "1A2E", "1A2F", "1A2G", "1A2H", "1A2I", "1A2J",
                      "1A2K", "1A2L", "1A2M", "1A3A2", "1A3B", 
                      "1A4A", "1A4B", "1A4C1", "1A4C2"]

    ## Fuels

    fin_tax_I_fuel_I = ["Oil", "Coal/peat", "Natural gas"]      
    
    ## Coverage dictionaries

    fin_tax_jur_coverage = {1990:fin_tax_jur_I,
                            1991:fin_tax_jur_I, 1992:fin_tax_jur_I,
                            1993:fin_tax_jur_I, 1994:fin_tax_jur_I,
                            1995:fin_tax_jur_I, 1996:fin_tax_jur_I,
                            1997:fin_tax_jur_I, 1998:fin_tax_jur_I,
                            1999:fin_tax_jur_I, 2000:fin_tax_jur_I,
                            2001:fin_tax_jur_I, 2002:fin_tax_jur_I,
                            2003:fin_tax_jur_I, 2004:fin_tax_jur_I,
                            2005:fin_tax_jur_I, 2006:fin_tax_jur_I,
                            2007:fin_tax_jur_I, 2008:fin_tax_jur_I,
                            2009:fin_tax_jur_I, 2010:fin_tax_jur_I,
                            2011:fin_tax_jur_I, 2012:fin_tax_jur_I,
                            2013:fin_tax_jur_I, 2014:fin_tax_jur_I,
                            2015:fin_tax_jur_I, 2016:fin_tax_jur_I,
                            2017:fin_tax_jur_I, 2018:fin_tax_jur_I,
                            2019:fin_tax_jur_I, 2020:fin_tax_jur_I,
                            2021:fin_tax_jur_I}

    fin_tax_ipcc_coverage = {1990:fin_tax_ipcc_I,
                             1991:fin_tax_ipcc_I, 1992:fin_tax_ipcc_I,
                             1993:fin_tax_ipcc_I, 1994:fin_tax_ipcc_I,
                             1995:fin_tax_ipcc_I, 1996:fin_tax_ipcc_I,
                             1997:fin_tax_ipcc_I, 1998:fin_tax_ipcc_I,
                             1999:fin_tax_ipcc_I, 2000:fin_tax_ipcc_I,
                             2001:fin_tax_ipcc_I, 2002:fin_tax_ipcc_I,
                             2003:fin_tax_ipcc_I, 2004:fin_tax_ipcc_I,
                             2005:fin_tax_ipcc_II, 2006:fin_tax_ipcc_II,
                             2007:fin_tax_ipcc_II, 2008:fin_tax_ipcc_II,
                             2009:fin_tax_ipcc_II, 2010:fin_tax_ipcc_II,
                             2011:fin_tax_ipcc_II, 2012:fin_tax_ipcc_II,
                             2013:fin_tax_ipcc_II, 2014:fin_tax_ipcc_II,
                             2015:fin_tax_ipcc_II, 2016:fin_tax_ipcc_II,
                             2017:fin_tax_ipcc_II, 2018:fin_tax_ipcc_II,
                             2019:fin_tax_ipcc_II, 2020:fin_tax_ipcc_II,
                             2021:fin_tax_ipcc_II}
    
    fin_tax_fuel_coverage = {1990:fin_tax_I_fuel_I,
                             1991:fin_tax_I_fuel_I, 1992:fin_tax_I_fuel_I,
                             1993:fin_tax_I_fuel_I, 1994:fin_tax_I_fuel_I,
                             1995:fin_tax_I_fuel_I, 1996:fin_tax_I_fuel_I,
                             1997:fin_tax_I_fuel_I, 1998:fin_tax_I_fuel_I,
                             1999:fin_tax_I_fuel_I, 2000:fin_tax_I_fuel_I,
                             2001:fin_tax_I_fuel_I, 2002:fin_tax_I_fuel_I,
                             2003:fin_tax_I_fuel_I, 2004:fin_tax_I_fuel_I,
                             2005:fin_tax_I_fuel_I, 2006:fin_tax_I_fuel_I,
                             2007:fin_tax_I_fuel_I, 2008:fin_tax_I_fuel_I,
                             2009:fin_tax_I_fuel_I, 2010:fin_tax_I_fuel_I,
                             2011:fin_tax_I_fuel_I, 2012:fin_tax_I_fuel_I,
                             2013:fin_tax_I_fuel_I, 2014:fin_tax_I_fuel_I,
                             2015:fin_tax_I_fuel_I, 2016:fin_tax_I_fuel_I,
                             2017:fin_tax_I_fuel_I, 2018:fin_tax_I_fuel_I,
                             2019:fin_tax_I_fuel_I, 2020:fin_tax_I_fuel_I,
                             2021:fin_tax_I_fuel_I}
    
    ## Sources dictionary
    
    fin_tax_coverage_sources = {1990:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])", 
                                1991:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])", 
                                1992:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])",
                                1993:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])", 
                                1994:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])",
                                1995:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])", 
                                1996:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])",
                                1997:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])", 
                                1998:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])",
                                1999:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])", 
                                2000:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])",
                                2001:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])", 
                                2002:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])",
                                2003:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])", 
                                2004:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])",
                                2005:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])", 
                                2006:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])",
                                2007:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])", 
                                2008:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])",
                                2009:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])", 
                                2010:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])",
                                2011:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])", 
                                2012:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])",
                                2013:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])", 
                                2014:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])",
                                2015:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])", 
                                2016:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])",
                                2017:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])", 
                                2018:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])",
                                2019:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])", 
                                2020:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])",
                                2021:"report(IEA-EPT[2015],WB[2014]),journal(VEH[2005]),web(USEPA[2015])"}

    #----------------------------------------------------------------------------

    # France
    
    ## Jurisdiction
    
    fra_tax_jur_I = ["France"]

    ## Sectors
    
    # initial coverage
    fra_tax_ipcc_I = ["1A1B", "1A1C",
                      "1A4A", "1A4B"]

    # extension to road transport (2015)
    fra_tax_ipcc_II = ["1A1B", "1A1C", "1A3B",
                      "1A4A", "1A4B"]

    ## Fuels
    
    fra_tax_fuel_I = ["Oil", "Natural gas", "Coal/peat"]

    ## Coverage dictionaries
    
    fra_tax_jur_coverage = {2014:fra_tax_jur_I, 2015:fra_tax_jur_I,
                            2016:fra_tax_jur_I, 2017:fra_tax_jur_I,
                            2018:fra_tax_jur_I, 2019:fra_tax_jur_I, 
                            2020:fra_tax_jur_I}
    
    fra_tax_ipcc_coverage = {2014:fra_tax_ipcc_I, 2015:fra_tax_ipcc_II,
                            2016:fra_tax_ipcc_II, 2017:fra_tax_ipcc_II,
                            2018:fra_tax_ipcc_II, 2019:fra_tax_ipcc_II, 
                            2020:fra_tax_ipcc_II}
    
    fra_tax_fuel_coverage = {2014:fra_tax_fuel_I, 2015:fra_tax_fuel_I,
                            2016:fra_tax_fuel_I, 2017:fra_tax_fuel_I,
                            2018:fra_tax_fuel_I, 2019:fra_tax_fuel_I, 
                            2020:fra_tax_fuel_I, 2021:fra_tax_fuel_I}

    ## Sources dictionary
    
    fra_tax_coverage_sources = {2014:"report(WB[2017]),news(LE-FRA[2020]),gvt(FRA[2019])", 
                                2015:"report(WB[2017]),news(LE-FRA[2020]),gvt(FRA[2019]),leg(FRA[2014])", 
                                2016:"report(WB[2017]),news(LE-FRA[2020]),gvt(FRA[2019]),leg(FRA[2014])",
                                2017:"report(WB[2017]),news(LE-FRA[2020]),gvt(FRA[2019]),leg(FRA[2014])", 
                                2018:"report(WB[2017]),news(LE-FRA[2020]),gvt(FRA[2019]),leg(FRA[2014])", 
                                2019:"report(WB[2017]),news(LE-FRA[2020]),gvt(FRA[2019]),leg(FRA[2014])", 
                                2020:"report(WB[2017]),news(LE-FRA[2020]),gvt(FRA[2019]),leg(FRA[2014])",
                                2021:"report(WB[2017]),news(LE-FRA[2020]),gvt(FRA[2019]),leg(FRA[2014])"}

    #----------------------------------------------------------------------------

    # Iceland
    
    ## Jurisdiction
    
    isl_tax_jur_I = ["Iceland"]

    ## Sectors
    
    # initial coverage
    isl_tax_ipcc_I = ["1A1B", "1A1C", "1A3B", "1A4A", "1A4B", 
                      "1A4C1", "1A4C2"]

    ## Fuels
    
    isl_tax_fuel_I = ["Oil"]

    ## Coverage dictionaries
    
    isl_tax_jur_coverage = {2010:isl_tax_jur_I, 2011:isl_tax_jur_I,
                            2012:isl_tax_jur_I, 2013:isl_tax_jur_I,
                            2014:isl_tax_jur_I, 2015:isl_tax_jur_I,
                            2016:isl_tax_jur_I, 2017:isl_tax_jur_I,
                            2018:isl_tax_jur_I, 2019:isl_tax_jur_I, 
                            2020:isl_tax_jur_I}
    
    isl_tax_ipcc_coverage = {2010:isl_tax_ipcc_I, 2011:isl_tax_ipcc_I,
                             2012:isl_tax_ipcc_I, 2013:isl_tax_ipcc_I,
                             2014:isl_tax_ipcc_I, 2015:isl_tax_ipcc_I,
                             2016:isl_tax_ipcc_I, 2017:isl_tax_ipcc_I,
                             2018:isl_tax_ipcc_I, 2019:isl_tax_ipcc_I, 
                             2020:isl_tax_ipcc_I}
    
    isl_tax_fuel_coverage = {2010:isl_tax_fuel_I, 2011:isl_tax_fuel_I,
                             2012:isl_tax_fuel_I, 2013:isl_tax_fuel_I,
                             2014:isl_tax_fuel_I, 2015:isl_tax_fuel_I,
                             2016:isl_tax_fuel_I, 2017:isl_tax_fuel_I,
                             2018:isl_tax_fuel_I, 2019:isl_tax_fuel_I, 
                             2020:isl_tax_fuel_I}

    ## Sources dictionary
    
    isl_tax_coverage_sources = {2010:"leg(ISL-ENRTA[2009])", 
                                2011:"leg(ISL-ENRTA[2009])", 
                                2012:"leg(ISL-ENRTA[2009])",
                                2013:"leg(ISL-ENRTA[2009])", 
                                2014:"leg(ISL-ENRTA[2009])", 
                                2015:"leg(ISL-ENRTA[2009])", 
                                2016:"leg(ISL-ENRTA[2009])",
                                2017:"leg(ISL-ENRTA[2009])", 
                                2018:"leg(ISL-ENRTA[2009])", 
                                2019:"leg(ISL-ENRTA[2009])", 
                                2020:"leg(ISL-ENRTA[2009])",
                                2021:"leg(ISL-ENRTA[2009])"}

    #----------------------------------------------------------------------------

    # Ireland
    
    ## Jurisdiction
    
    irl_tax_jur_I = ["Ireland"]

    ## Sectors
    
    # initial coverage
    irl_tax_ipcc_I = ["1A3A2", "1A3B", "1A3D1", 
                      "1A3D1", "1A3D2", "1A3E1", "1A4A", "1A4B", "1A4C1"]

    ## Fuels
    
    irl_tax_fuel_I = ["Oil", "Natural gas"]
    irl_tax_fuel_II = ["Oil", "Natural gas", "Coal/peat"]

    ## Coverage dictionaries
    
    irl_tax_jur_coverage = {2010:irl_tax_jur_I, 2011:irl_tax_jur_I,
                            2012:irl_tax_jur_I, 2013:irl_tax_jur_I,
                            2014:irl_tax_jur_I, 2015:irl_tax_jur_I,
                            2016:irl_tax_jur_I, 2017:irl_tax_jur_I,
                            2018:irl_tax_jur_I, 2019:irl_tax_jur_I, 
                            2020:irl_tax_jur_I}
    
    irl_tax_ipcc_coverage = {2010:irl_tax_ipcc_I, 2011:irl_tax_ipcc_I,
                             2012:irl_tax_ipcc_I, 2013:irl_tax_ipcc_I,
                             2014:irl_tax_ipcc_I, 2015:irl_tax_ipcc_I,
                             2016:irl_tax_ipcc_I, 2017:irl_tax_ipcc_I,
                             2018:irl_tax_ipcc_I, 2019:irl_tax_ipcc_I, 
                             2020:irl_tax_ipcc_I}
    
    irl_tax_fuel_coverage = {2010:irl_tax_fuel_I, 2011:irl_tax_fuel_I,
                             2012:irl_tax_fuel_I, 2013:irl_tax_fuel_II,
                             2014:irl_tax_fuel_II, 2015:irl_tax_fuel_I,
                             2016:irl_tax_fuel_II, 2017:irl_tax_fuel_II,
                             2018:irl_tax_fuel_II, 2019:irl_tax_fuel_II, 
                             2020:irl_tax_fuel_II}
    
    ## Sources dictionary
    
    irl_tax_coverage_sources = {2010:"leg(IRL-FA[2010])", 2011:"leg(IRL-FA[2010])", 
                                2012:"leg(IRL-FA[2010])", 2013:"leg(IRL-FA[2010])", 
                                2014:"leg(IRL-FA[2010])", 2015:"leg(IRL-FA[2010])", 
                                2016:"leg(IRL-FA[2010])", 2017:"leg(IRL-FA[2010])", 
                                2018:"leg(IRL-FA[2010])", 2019:"leg(IRL-FA[2010])", 
                                2020:"leg(IRL-FA[2010])", 2021:"leg(IRL-FA[2010])"}

    #----------------------------------------------------------------------------

    # Japan
    
    ## Jurisdiction
    
    jpn_tax_jur_I = ["Japan"]

    ## Sectors
    
    # initial coverage
    jpn_tax_ipcc_I = ["1A1A1", "1A1A2", "1A1A3",
                      "1A2A", "1A2B", "1A2C", "1A2D", "1A2E", "1A2F", "1A2G", 
                      "1A2H", "1A2I", "1A2J", "1A2K", "1A2L", "1A2M",
                      "1A3B"]

    ## Fuels
    
    jpn_tax_fuel_I = ["Oil", "Natural gas", "Coal/peat"]

    ## Coverage dictionaries
    
    jpn_tax_jur_coverage = {2012:jpn_tax_jur_I, 2013:jpn_tax_jur_I,
                            2014:jpn_tax_jur_I, 2015:jpn_tax_jur_I,
                            2016:jpn_tax_jur_I, 2017:jpn_tax_jur_I,
                            2018:jpn_tax_jur_I, 2019:jpn_tax_jur_I, 
                            2020:jpn_tax_jur_I}
    
    jpn_tax_ipcc_coverage = {2012:jpn_tax_ipcc_I, 2013:jpn_tax_ipcc_I,
                             2014:jpn_tax_ipcc_I, 2015:jpn_tax_ipcc_I,
                             2016:jpn_tax_ipcc_I, 2017:jpn_tax_ipcc_I,
                             2018:jpn_tax_ipcc_I, 2019:jpn_tax_ipcc_I, 
                             2020:jpn_tax_ipcc_I}
    
    jpn_tax_fuel_coverage = {2012:jpn_tax_fuel_I, 2013:jpn_tax_fuel_I,
                             2014:jpn_tax_fuel_I, 2015:jpn_tax_fuel_I,
                             2016:jpn_tax_fuel_I, 2017:jpn_tax_fuel_I,
                             2018:jpn_tax_fuel_I, 2019:jpn_tax_fuel_I, 
                             2020:jpn_tax_fuel_I}
    
    ## Sources dictionary
    
    jpn_tax_coverage_sources = {2012:"leg(JP[2012]), gvt(MEJ-CT[2014])",
                                2013:"leg(JP[2012]), gvt(MEJ-CT[2014])", 
                                2014:"leg(JP[2012]), gvt(MEJ-CT[2014])", 
                                2015:"leg(JP[2012]), gvt(MEJ-CT[2014])", 
                                2016:"leg(JP[2012]), gvt(MEJ-CT[2014])",
                                2017:"leg(JP[2012]), gvt(MEJ-CT[2014])", 
                                2018:"leg(JP[2012]), gvt(MEJ-CT[2014])", 
                                2019:"leg(JP[2012]), gvt(MEJ-CT[2014])", 
                                2020:"leg(JP[2012]), gvt(MEJ-CT[2014])",
                                2021:"leg(JP[2012]), gvt(MEJ-CT[2014])"}

    #----------------------------------------------------------------------------

    # Latvia
    
    ## Jurisdiction
    
    lva_tax_jur_I = ["Latvia"]

    ## Sectors
    
    # initial coverage
    lva_tax_ipcc_I = ["1A1A1", "1A1A2", "1A1A3", 
                      "1A2A", "1A2B", "1A2C", "1A2D", "1A2E", "1A2F", "1A2G", 
                      "1A2H", "1A2I", "1A2J", "1A2K", "1A2L", "1A2M"]

    ## Fuels
    
    lva_tax_fuel_I = ["Oil", "Natural gas", "Coal/peat"]

    ## Coverage dictionaries
    
    lva_tax_jur_coverage = {2004:lva_tax_jur_I, 2005:lva_tax_jur_I,
                            2006:lva_tax_jur_I, 2007:lva_tax_jur_I,
                            2008:lva_tax_jur_I, 2009:lva_tax_jur_I,
                            2010:lva_tax_jur_I, 2011:lva_tax_jur_I,
                            2012:lva_tax_jur_I, 2013:lva_tax_jur_I,
                            2014:lva_tax_jur_I, 2015:lva_tax_jur_I,
                            2016:lva_tax_jur_I, 2017:lva_tax_jur_I,
                            2018:lva_tax_jur_I, 2019:lva_tax_jur_I, 
                            2020:lva_tax_jur_I}
    
    lva_tax_ipcc_coverage = {2004:lva_tax_ipcc_I, 2005:lva_tax_ipcc_I,
                             2006:lva_tax_ipcc_I, 2007:lva_tax_ipcc_I,
                             2008:lva_tax_ipcc_I, 2009:lva_tax_ipcc_I,
                             2010:lva_tax_ipcc_I, 2011:lva_tax_ipcc_I,
                             2012:lva_tax_ipcc_I, 2013:lva_tax_ipcc_I,
                             2014:lva_tax_ipcc_I, 2015:lva_tax_ipcc_I,
                             2016:lva_tax_ipcc_I, 2017:lva_tax_ipcc_I,
                             2018:lva_tax_ipcc_I, 2019:lva_tax_ipcc_I, 
                             2020:lva_tax_ipcc_I}
    
    lva_tax_fuel_coverage = {2004:lva_tax_fuel_I, 2005:lva_tax_fuel_I,
                             2006:lva_tax_fuel_I, 2007:lva_tax_fuel_I,
                             2008:lva_tax_fuel_I, 2009:lva_tax_fuel_I,
                             2010:lva_tax_fuel_I, 2011:lva_tax_fuel_I,
                             2012:lva_tax_fuel_I, 2013:lva_tax_fuel_I,
                             2014:lva_tax_fuel_I, 2015:lva_tax_fuel_I,
                             2016:lva_tax_fuel_I, 2017:lva_tax_fuel_I,
                             2018:lva_tax_fuel_I, 2019:lva_tax_fuel_I, 
                             2020:lva_tax_fuel_I}

    ## Sources dictionary
    
    lva_tax_coverage_sources = {2004:"leg(LV-NRTL[2005])", 2005:"leg(LV-NRTL[2005])", 
                                2006:"leg(LV-NRTL[2005])", 2007:"leg(LV-NRTL[2005])", 
                                2008:"leg(LV-NRTL[2005])", 2009:"leg(LV-NRTL[2005])",
                                2010:"leg(LV-NRTL[2005])", 2011:"leg(LV-NRTL[2005])", 
                                2012:"leg(LV-NRTL[2005])", 2013:"leg(LV-NRTL[2005])", 
                                2014:"leg(LV-NRTL[2005])", 2015:"leg(LV-NRTL[2005])", 
                                2016:"leg(LV-NRTL[2005])", 2017:"leg(LV-NRTL[2005])", 
                                2018:"leg(LV-NRTL[2005])", 2019:"leg(LV-NRTL[2005])", 
                                2020:"leg(LV-NRTL[2005])", 2021:"leg(LV-NRTL[2005])"}

    #----------------------------------------------------------------------------

    # Liechtenstein
    
    ## Jurisdiction
    
    lie_tax_jur_I = ["Liechstenstein"]

    ## Sectors
    
    # initial coverage
    lie_tax_ipcc_I = ["1A1A2", "1A1A3", "1A4B"]

    ## Fuels
    
    lie_tax_fuel_I = ["Oil", "Natural gas", "Coal/peat"]

    ## Coverage dictionaries
    
    lie_tax_jur_coverage = {2008:lie_tax_jur_I, 2009:lie_tax_jur_I,
                            2010:lie_tax_jur_I, 2011:lie_tax_jur_I,
                            2012:lie_tax_jur_I, 2013:lie_tax_jur_I,
                            2014:lie_tax_jur_I, 2015:lie_tax_jur_I,
                            2016:lie_tax_jur_I, 2017:lie_tax_jur_I,
                            2018:lie_tax_jur_I, 2019:lie_tax_jur_I, 
                            2020:lie_tax_jur_I}
    
    lie_tax_ipcc_coverage = {2008:lie_tax_ipcc_I, 2009:lie_tax_ipcc_I,
                             2010:lie_tax_ipcc_I, 2011:lie_tax_ipcc_I,
                             2012:lie_tax_ipcc_I, 2013:lie_tax_ipcc_I,
                             2014:lie_tax_ipcc_I, 2015:lie_tax_ipcc_I,
                             2016:lie_tax_ipcc_I, 2017:lie_tax_ipcc_I,
                             2018:lie_tax_ipcc_I, 2019:lie_tax_ipcc_I, 
                             2020:lie_tax_ipcc_I}
    
    lie_tax_fuel_coverage = {2008:lie_tax_fuel_I, 2009:lie_tax_fuel_I,
                             2010:lie_tax_fuel_I, 2011:lie_tax_fuel_I,
                             2012:lie_tax_fuel_I, 2013:lie_tax_fuel_I,
                             2014:lie_tax_fuel_I, 2015:lie_tax_fuel_I,
                             2016:lie_tax_fuel_I, 2017:lie_tax_fuel_I,
                             2018:lie_tax_fuel_I, 2019:lie_tax_fuel_I, 
                             2020:lie_tax_fuel_I}
    
    ## Sources dictionary
    
    lie_tax_coverage_sources = {2008:"gvt(CH[2005], CH[2009])", 
                                2009:"gvt(CH[2005], CH[2009])",
                                2010:"gvt(CH[2005], CH[2009])", 
                                2011:"gvt(CH[2005], CH[2009])", 
                                2012:"gvt(CH[2005], CH[2009])",
                                2013:"gvt(CH[2005], CH[2009])", 
                                2014:"leg(CHE-CO2[2013], CHE-FARC[2013])", 
                                2015:"leg(CHE-CO2[2013], CHE-FARC[2013])", 
                                2016:"leg(CHE-CO2[2013], CHE-FARC[2013])",
                                2017:"leg(CHE-CO2[2013], CHE-FARC[2013])", 
                                2018:"leg(CHE-CO2[2013], CHE-FARC[2013])", 
                                2019:"leg(CHE-CO2[2013], CHE-FARC[2013])", 
                                2020:"leg(CHE-CO2[2013], CHE-FARC[2013])",
                                2021:"leg(CHE-CO2[2013], CHE-FARC[2013])"}

    #----------------------------------------------------------------------------

    # Mexico
    
    ## Jurisdiction
    
    mex_tax_jur_I = ["Mexico"]

    ## Sectors
    
    mex_tax_ipcc_I = ["1A1A1", "1A1B", "1A1C", 
                      "1A2A", "1A2B", "1A2C", "1A2D", "1A2E", "1A2F", "1A2G", 
                      "1A2H", "1A2I", "1A2J", "1A2K", "1A2L", "1A2M",
                      "1A3A2", "1A3B", "1A4B", "1A4C1"]
    
    ## Fuels
    
    mex_tax_fuel_I = ["Oil", "Coal/peat"]

    ## Coverage dictionaries
    
    mex_tax_jur_coverage = {2014:mex_tax_jur_I, 2015:mex_tax_jur_I,
                            2016:mex_tax_jur_I, 2017:mex_tax_jur_I,
                            2018:mex_tax_jur_I, 2019:mex_tax_jur_I, 
                            2020:mex_tax_jur_I, 2021:mex_tax_jur_I}
    
    mex_tax_ipcc_coverage = {2014:mex_tax_ipcc_I, 2015:mex_tax_ipcc_I,
                             2016:mex_tax_ipcc_I, 2017:mex_tax_ipcc_I,
                             2018:mex_tax_ipcc_I, 2019:mex_tax_ipcc_I, 
                             2020:mex_tax_ipcc_I, 2021:mex_tax_ipcc_I}
    
    mex_tax_fuel_coverage = {2014:mex_tax_fuel_I, 2015:mex_tax_fuel_I,
                             2016:mex_tax_fuel_I, 2017:mex_tax_fuel_I,
                             2018:mex_tax_fuel_I, 2019:mex_tax_fuel_I, 
                             2020:mex_tax_fuel_I, 2021:mex_tax_fuel_I}
    
    ## Sources dictionary
    
    mex_tax_coverage_sources = {2014:"leg(LIEP[2012])", 2015:"leg(LIEP[2012])", 
                                2016:"leg(LIEP[2012])", 2017:"leg(LIEP[2012])", 
                                2018:"leg(LIEP[2012])", 2019:"leg(LIEP[2012])", 
                                2020:"leg(LIEP[2012])", 2021:"leg(LIEP[2012])"}

    #----------------------------------------------------------------------------

    # Norway
    
    ## Jurisdictions    
    
    nor_tax_I_jur_I = ["Norway"]
    nor_tax_II_jur_I = ["Norway"]
    
    ## Sectors
    nor_tax_I_ipcc_I = ["1A1A1", "1A1B", "1A1C", "1A2A", "1A2B", "1A2C",
                        "1A2D", "1A2E", "1A2F", "1A2G", "1A2H", "1A2I", "1A2J",
                        "1A2K", "1A2L", "1A2M", "1A3A2", "1A3B", "1A4A", "1A4B",
                        "1A4C2"]
    
    nor_tax_I_ipcc_II = ["1A1B", "1A1C", "1A3A2", "1A3B", "1A4A", "1A4B",
                         "1A4C2"]
    
    nor_tax_II_ipcc_I = ["1B2A1", "1B2A2", "1B2A32", "1B2A33"]
    
    ## Fuels

    nor_tax_I_fuel_I = ["Oil"]
    nor_tax_I_fuel_II = ["Oil", "Natural gas"]
    
    nor_tax_II_fuel_I = ["Oil", "Natural gas"]    
     
    
    ## Coverage dictionaries

    nor_tax_I_jur_coverage = {1991:nor_tax_I_jur_I, 1992:nor_tax_I_jur_I,
                              1993:nor_tax_I_jur_I, 1994:nor_tax_I_jur_I,
                              1995:nor_tax_I_jur_I, 1996:nor_tax_I_jur_I,
                              1997:nor_tax_I_jur_I, 1998:nor_tax_I_jur_I,
                              1999:nor_tax_I_jur_I, 2000:nor_tax_I_jur_I,
                              2001:nor_tax_I_jur_I, 2002:nor_tax_I_jur_I,
                              2003:nor_tax_I_jur_I, 2004:nor_tax_I_jur_I,
                              2005:nor_tax_I_jur_I, 2006:nor_tax_I_jur_I,
                              2007:nor_tax_I_jur_I, 2008:nor_tax_I_jur_I,
                              2009:nor_tax_I_jur_I, 2010:nor_tax_I_jur_I,
                              2011:nor_tax_I_jur_I, 2012:nor_tax_I_jur_I,
                              2013:nor_tax_I_jur_I, 2014:nor_tax_I_jur_I,
                              2015:nor_tax_I_jur_I, 2016:nor_tax_I_jur_I,
                              2017:nor_tax_I_jur_I, 2018:nor_tax_I_jur_I,
                              2019:nor_tax_I_jur_I, 2020:nor_tax_I_jur_I,
                              2021:nor_tax_I_jur_I}

    nor_tax_I_ipcc_coverage = {1991:nor_tax_I_ipcc_I, 1992:nor_tax_I_ipcc_I,
                               1993:nor_tax_I_ipcc_I, 1994:nor_tax_I_ipcc_I,
                               1995:nor_tax_I_ipcc_I, 1996:nor_tax_I_ipcc_I,
                               1997:nor_tax_I_ipcc_I, 1998:nor_tax_I_ipcc_I,
                               1999:nor_tax_I_ipcc_I, 2000:nor_tax_I_ipcc_I,
                               2001:nor_tax_I_ipcc_I, 2002:nor_tax_I_ipcc_I,
                               2003:nor_tax_I_ipcc_I, 2004:nor_tax_I_ipcc_I,
                               2005:nor_tax_I_ipcc_I, 2006:nor_tax_I_ipcc_I,
                               2007:nor_tax_I_ipcc_I, 2008:nor_tax_I_ipcc_II,
                               2009:nor_tax_I_ipcc_II, 2010:nor_tax_I_ipcc_II,
                               2011:nor_tax_I_ipcc_II, 2012:nor_tax_I_ipcc_II,
                               2013:nor_tax_I_ipcc_II, 2014:nor_tax_I_ipcc_II,
                               2015:nor_tax_I_ipcc_II, 2016:nor_tax_I_ipcc_II,
                               2017:nor_tax_I_ipcc_II, 2018:nor_tax_I_ipcc_II,
                               2019:nor_tax_I_ipcc_II, 2020:nor_tax_I_ipcc_II,
                               2021:nor_tax_I_ipcc_II}
    
    nor_tax_I_fuel_coverage = {1991:nor_tax_I_fuel_I, 1992:nor_tax_I_fuel_I,
                               1993:nor_tax_I_fuel_I, 1994:nor_tax_I_fuel_I,
                               1995:nor_tax_I_fuel_I, 1996:nor_tax_I_fuel_I,
                               1997:nor_tax_I_fuel_I, 1998:nor_tax_I_fuel_I,
                               1999:nor_tax_I_fuel_I, 2000:nor_tax_I_fuel_I,
                               2001:nor_tax_I_fuel_I, 2002:nor_tax_I_fuel_I,
                               2003:nor_tax_I_fuel_I, 2004:nor_tax_I_fuel_I,
                               2005:nor_tax_I_fuel_I, 2006:nor_tax_I_fuel_I,
                               2007:nor_tax_I_fuel_II, 2008:nor_tax_I_fuel_II,
                               2009:nor_tax_I_fuel_II, 2010:nor_tax_I_fuel_II,
                               2011:nor_tax_I_fuel_II, 2012:nor_tax_I_fuel_II,
                               2013:nor_tax_I_fuel_II, 2014:nor_tax_I_fuel_II,
                               2015:nor_tax_I_fuel_II, 2016:nor_tax_I_fuel_II,
                               2017:nor_tax_I_fuel_II, 2018:nor_tax_I_fuel_II,
                               2019:nor_tax_I_fuel_II, 2020:nor_tax_I_fuel_II,
                               2021:nor_tax_I_fuel_II}


    nor_tax_II_jur_coverage = {1991:nor_tax_II_jur_I, 1992:nor_tax_II_jur_I,
                               1993:nor_tax_II_jur_I, 1994:nor_tax_II_jur_I,
                               1995:nor_tax_II_jur_I, 1996:nor_tax_II_jur_I,
                               1997:nor_tax_II_jur_I, 1998:nor_tax_II_jur_I,
                               1999:nor_tax_II_jur_I, 2000:nor_tax_II_jur_I,
                               2001:nor_tax_II_jur_I, 2002:nor_tax_II_jur_I,
                               2003:nor_tax_II_jur_I, 2004:nor_tax_II_jur_I,
                               2005:nor_tax_II_jur_I, 2006:nor_tax_II_jur_I,
                               2007:nor_tax_II_jur_I, 2008:nor_tax_II_jur_I,
                               2009:nor_tax_II_jur_I, 2010:nor_tax_II_jur_I,
                               2011:nor_tax_II_jur_I, 2012:nor_tax_II_jur_I,
                               2013:nor_tax_II_jur_I, 2014:nor_tax_II_jur_I,
                               2015:nor_tax_II_jur_I, 2016:nor_tax_II_jur_I,
                               2017:nor_tax_II_jur_I, 2018:nor_tax_II_jur_I,
                               2019:nor_tax_II_jur_I, 2020:nor_tax_II_jur_I,
                               2021:nor_tax_II_jur_I}

    nor_tax_II_ipcc_coverage = {1991:nor_tax_II_ipcc_I, 1992:nor_tax_II_ipcc_I,
                               1993:nor_tax_II_ipcc_I, 1994:nor_tax_II_ipcc_I,
                               1995:nor_tax_II_ipcc_I, 1996:nor_tax_II_ipcc_I,
                               1997:nor_tax_II_ipcc_I, 1998:nor_tax_II_ipcc_I,
                               1999:nor_tax_II_ipcc_I, 2000:nor_tax_II_ipcc_I,
                               2001:nor_tax_II_ipcc_I, 2002:nor_tax_II_ipcc_I,
                               2003:nor_tax_II_ipcc_I, 2004:nor_tax_II_ipcc_I,
                               2005:nor_tax_II_ipcc_I, 2006:nor_tax_II_ipcc_I,
                               2007:nor_tax_II_ipcc_I, 2008:nor_tax_II_ipcc_I,
                               2009:nor_tax_II_ipcc_I, 2010:nor_tax_II_ipcc_I,
                               2011:nor_tax_II_ipcc_I, 2012:nor_tax_II_ipcc_I,
                               2013:nor_tax_II_ipcc_I, 2014:nor_tax_II_ipcc_I,
                               2015:nor_tax_II_ipcc_I, 2016:nor_tax_II_ipcc_I,
                               2017:nor_tax_II_ipcc_I, 2018:nor_tax_II_ipcc_I,
                               2019:nor_tax_II_ipcc_I, 2020:nor_tax_II_ipcc_I,
                               2021:nor_tax_II_ipcc_I}
    
    nor_tax_II_fuel_coverage = {1991:nor_tax_II_fuel_I, 1992:nor_tax_II_fuel_I,
                               1993:nor_tax_II_fuel_I, 1994:nor_tax_II_fuel_I,
                               1995:nor_tax_II_fuel_I, 1996:nor_tax_II_fuel_I,
                               1997:nor_tax_II_fuel_I, 1998:nor_tax_II_fuel_I,
                               1999:nor_tax_II_fuel_I, 2000:nor_tax_II_fuel_I,
                               2001:nor_tax_II_fuel_I, 2002:nor_tax_II_fuel_I,
                               2003:nor_tax_II_fuel_I, 2004:nor_tax_II_fuel_I,
                               2005:nor_tax_II_fuel_I, 2006:nor_tax_II_fuel_I,
                               2007:nor_tax_II_fuel_I, 2008:nor_tax_II_fuel_I,
                               2009:nor_tax_II_fuel_I, 2010:nor_tax_II_fuel_I,
                               2011:nor_tax_II_fuel_I, 2012:nor_tax_II_fuel_I,
                               2013:nor_tax_II_fuel_I, 2014:nor_tax_II_fuel_I,                              
                               2015:nor_tax_II_fuel_I, 2016:nor_tax_II_fuel_I,
                               2017:nor_tax_II_fuel_I, 2018:nor_tax_II_fuel_I,
                               2019:nor_tax_II_fuel_I, 2020:nor_tax_II_fuel_I,
                               2021:nor_tax_II_fuel_I}
    
    
    ## Sources dictionary
    
    nor_tax_I_coverage_sources = {1991:"leg(NOR-EA[1990])", 1992:"leg(NOR-EA[1990])",
                                  1993:"leg(NOR-EA[1990])", 1994:"leg(NOR-EA[1990])",
                                  1995:"leg(NOR-EA[1990])", 1996:"leg(NOR-EA[1990])",
                                  1997:"leg(NOR-EA[1990])", 1998:"leg(NOR-EA[1990])",
                                  1999:"leg(NOR-EA[1990])", 2000:"leg(NOR-EA[1990])",
                                  2001:"leg(NOR-EA[1990])", 2002:"leg(NOR-EA[1990])",
                                  2003:"leg(NOR-EA[1990])", 2004:"leg(NOR-EA[1990])",
                                  2005:"leg(NOR-EA[1990])", 2006:"leg(NOR-EA[1990])",
                                  2007:"leg(NOR-EA[1990])", 2008:"leg(NOR-EA[1990])",
                                  2009:"leg(NOR-EA[1990])", 2010:"leg(NOR-EA[1990])",
                                  2011:"leg(NOR-EA[1990])", 2012:"leg(NOR-EA[1990])",
                                  2013:"leg(NOR-EA[1990])", 2014:"leg(NOR-EA[1990])",
                                  2015:"leg(NOR-EA[1990])", 2016:"leg(NOR-EA[1990])",
                                  2017:"leg(NOR-EA[1990])", 2018:"leg(NOR-EA[1990])",
                                  2019:"leg(NOR-EA[1990])", 2020:"leg(NOR-EA[1990])",
                                  2021:"leg(NOR-EA[1990])"}
    
    nor_tax_II_coverage_sources = {1991:"leg(NOR[1990])", 1992:"leg(NOR[1990])",
                                   1993:"leg(NOR[1990])", 1994:"leg(NOR[1990])",
                                   1995:"leg(NOR[1990])", 1996:"leg(NOR[1990])",
                                   1997:"leg(NOR[1990])", 1998:"leg(NOR[1990])",
                                   1999:"leg(NOR[1990])", 2000:"leg(NOR[1990])",
                                   2001:"leg(NOR[1990])", 2002:"leg(NOR[1990])",
                                   2003:"leg(NOR[1990])", 2004:"leg(NOR[1990])",
                                   2005:"leg(NOR[1990])", 2006:"leg(NOR[1990])",
                                   2007:"leg(NOR[1990])", 2008:"leg(NOR[1990])",
                                   2009:"leg(NOR[1990])", 2010:"leg(NOR[1990])",
                                   2011:"leg(NOR[1990])", 2012:"leg(NOR[1990])",
                                   2013:"leg(NOR[1990])", 2014:"leg(NOR[1990])",
                                   2015:"leg(NOR[1990])", 2016:"leg(NOR[1990])",
                                   2017:"leg(NOR[1990])", 2018:"leg(NOR[1990])",
                                   2019:"leg(NOR[1990])", 2020:"leg(NOR[1990])",
                                   2021:"leg(NOR[1990])"}
    
    
    #----------------------------------------------------------------------------

    # Poland
    
    ## Jurisdictions    
    
    pol_tax_jur_I = ["Poland"]
    
    ## Sectors
    pol_tax_ipcc_I = ["1A1A1", "1A2A", "1A2B", "1A2C", "1A2D", "1A2E", "1A2F", 
                      "1A2G", "1A2H", "1A2I", "1A2J", "1A2K", "1A2L", "1A2M"]
    
    
    ## Fuels

    pol_tax_fuel_I = ["Oil", "Coal/peat", "Natural gas"]      
    
    ## Coverage dictionaries

    pol_tax_jur_coverage = {1990:pol_tax_jur_I,
                            1991:pol_tax_jur_I, 1992:pol_tax_jur_I,
                            1993:pol_tax_jur_I, 1994:pol_tax_jur_I,
                            1995:pol_tax_jur_I, 1996:pol_tax_jur_I,
                            1997:pol_tax_jur_I, 1998:pol_tax_jur_I,
                            1999:pol_tax_jur_I, 2000:pol_tax_jur_I,
                            2001:pol_tax_jur_I, 2002:pol_tax_jur_I,
                            2003:pol_tax_jur_I, 2004:pol_tax_jur_I,
                            2005:pol_tax_jur_I, 2006:pol_tax_jur_I,
                            2007:pol_tax_jur_I, 2008:pol_tax_jur_I,
                            2009:pol_tax_jur_I, 2010:pol_tax_jur_I,
                            2011:pol_tax_jur_I, 2012:pol_tax_jur_I,
                            2013:pol_tax_jur_I, 2014:pol_tax_jur_I,
                            2015:pol_tax_jur_I, 2016:pol_tax_jur_I,
                            2017:pol_tax_jur_I, 2018:pol_tax_jur_I,
                            2019:pol_tax_jur_I, 2020:pol_tax_jur_I,
                            2021:pol_tax_jur_I}

    pol_tax_ipcc_coverage = {1990:pol_tax_ipcc_I,
                             1991:pol_tax_ipcc_I, 1992:pol_tax_ipcc_I,
                             1993:pol_tax_ipcc_I, 1994:pol_tax_ipcc_I,
                             1995:pol_tax_ipcc_I, 1996:pol_tax_ipcc_I,
                             1997:pol_tax_ipcc_I, 1998:pol_tax_ipcc_I,
                             1999:pol_tax_ipcc_I, 2000:pol_tax_ipcc_I,
                             2001:pol_tax_ipcc_I, 2002:pol_tax_ipcc_I,
                             2003:pol_tax_ipcc_I, 2004:pol_tax_ipcc_I,
                             2005:pol_tax_ipcc_I, 2006:pol_tax_ipcc_I,
                             2007:pol_tax_ipcc_I, 2008:pol_tax_ipcc_I,
                             2009:pol_tax_ipcc_I, 2010:pol_tax_ipcc_I,
                             2011:pol_tax_ipcc_I, 2012:pol_tax_ipcc_I,
                             2013:pol_tax_ipcc_I, 2014:pol_tax_ipcc_I,
                             2015:pol_tax_ipcc_I, 2016:pol_tax_ipcc_I,
                             2017:pol_tax_ipcc_I, 2018:pol_tax_ipcc_I,
                             2019:pol_tax_ipcc_I, 2020:pol_tax_ipcc_I,
                             2021:pol_tax_ipcc_I}

    pol_tax_fuel_coverage = {1990:pol_tax_fuel_I,
                             1991:pol_tax_fuel_I, 1992:pol_tax_fuel_I,
                             1993:pol_tax_fuel_I, 1994:pol_tax_fuel_I,
                             1995:pol_tax_fuel_I, 1996:pol_tax_fuel_I,
                             1997:pol_tax_fuel_I, 1998:pol_tax_fuel_I,
                             1999:pol_tax_fuel_I, 2000:pol_tax_fuel_I,
                             2001:pol_tax_fuel_I, 2002:pol_tax_fuel_I,
                             2003:pol_tax_fuel_I, 2004:pol_tax_fuel_I,
                             2005:pol_tax_fuel_I, 2006:pol_tax_fuel_I,
                             2007:pol_tax_fuel_I, 2008:pol_tax_fuel_I,
                             2009:pol_tax_fuel_I, 2010:pol_tax_fuel_I,
                             2011:pol_tax_fuel_I, 2012:pol_tax_fuel_I,
                             2013:pol_tax_fuel_I, 2014:pol_tax_fuel_I,
                             2015:pol_tax_fuel_I, 2016:pol_tax_fuel_I,
                             2017:pol_tax_fuel_I, 2018:pol_tax_fuel_I,
                             2019:pol_tax_fuel_I, 2020:pol_tax_fuel_I,
                             2021:pol_tax_fuel_I}
    
    ## Sources dictionary
    
    pol_tax_coverage_sources = {1990:"report(OCED[2012], OECD-EP-P[2015])",
                                1991:"report(OCED[2012], OECD-EP-P[2015])", 
                                1992:"report(OCED[2012], OECD-EP-P[2015])",
                                1993:"report(OCED[2012], OECD-EP-P[2015])", 
                                1994:"report(OCED[2012], OECD-EP-P[2015])",
                                1995:"report(OCED[2012], OECD-EP-P[2015])", 
                                1996:"report(OCED[2012], OECD-EP-P[2015])",
                                1997:"report(OCED[2012], OECD-EP-P[2015])", 
                                1998:"report(OCED[2012], OECD-EP-P[2015])",
                                1999:"report(OCED[2012], OECD-EP-P[2015])", 
                                2000:"report(OCED[2012], OECD-EP-P[2015])",
                                2001:"report(OCED[2012], OECD-EP-P[2015])", 
                                2002:"report(OCED[2012], OECD-EP-P[2015])",
                                2003:"report(OCED[2012], OECD-EP-P[2015])", 
                                2004:"report(OCED[2012], OECD-EP-P[2015])",
                                2005:"report(OCED[2012], OECD-EP-P[2015])", 
                                2006:"report(OCED[2012], OECD-EP-P[2015])",
                                2007:"report(OCED[2012], OECD-EP-P[2015])", 
                                2008:"report(OCED[2012], OECD-EP-P[2015])",
                                2009:"report(OCED[2012], OECD-EP-P[2015])", 
                                2010:"report(OCED[2012], OECD-EP-P[2015])",
                                2011:"report(OCED[2012], OECD-EP-P[2015])", 
                                2012:"report(OCED[2012], OECD-EP-P[2015])",
                                2013:"report(OCED[2012], OECD-EP-P[2015])", 
                                2014:"report(OCED[2012], OECD-EP-P[2015])",
                                2015:"report(OCED[2012], OECD-EP-P[2015])", 
                                2016:"report(OCED[2012], OECD-EP-P[2015])",
                                2017:"report(OCED[2012], OECD-EP-P[2015])", 
                                2018:"report(OCED[2012], OECD-EP-P[2015])",
                                2019:"report(OCED[2012], OECD-EP-P[2015])", 
                                2020:"report(OCED[2012], OECD-EP-P[2015])",
                                2021:"report(OCED[2012], OECD-EP-P[2015])"}
    
    
    #----------------------------------------------------------------------------
    
    # Portugal
    
    ## Jurisdiction
    
    prt_tax_jur_I = ["Portugal"]

    ## Sectors
    
    prt_tax_ipcc_I = ["1A1A2", "1A1A3", "1A1B", "1A1C",
                      "1A3A1", "1A3B", "1A4A", "1A4B", "1A4C1", "1A4C2"]
    
    ## Fuels
    
    prt_tax_fuel_I = ["Oil", "Natural gas", "Coal/peat"]

    ## Coverage dictionaries
    
    prt_tax_jur_coverage = {2017:prt_tax_jur_I, 2018:prt_tax_jur_I, 
                            2019:prt_tax_jur_I, 2020:prt_tax_jur_I, 
                            2021:prt_tax_jur_I}
    
    prt_tax_ipcc_coverage = {2017:prt_tax_ipcc_I, 2018:prt_tax_ipcc_I, 
                             2019:prt_tax_ipcc_I, 2020:prt_tax_ipcc_I, 
                             2021:prt_tax_ipcc_I}     

    prt_tax_fuel_coverage = {2017:prt_tax_fuel_I, 2018:prt_tax_fuel_I, 
                             2019:prt_tax_fuel_I, 2020:prt_tax_fuel_I, 
                             2021:prt_tax_fuel_I}     

    ## Sources dictionary
    
    prt_tax_coverage_sources = {2017:"leg(PRT[2014]), gvt(PRT[2014])", 
                                2018:"leg(PRT[2014]), gvt(PRT[2014])", 
                                2019:"leg(PRT[2014]), gvt(PRT[2014])", 
                                2020:"leg(PRT[2014]), gvt(PRT[2014])",
                                2021:"leg(PRT[2014]), gvt(PRT[2014])"}

    #----------------------------------------------------------------------------

    # Singapore 
    
    ## Jurisdiction
    
    sgp_tax_jur_I = ["Singapore"]
    
    
    ## Sectors
    
    sgp_tax_ipcc_I = ["1A1A1", "1A1A2", "1A1A3", "1A1B", "1A1C", "1A2A", "1A2B",
                     "1A2C", "1A2D", "1A2E", "1A2F", "1A2G", "1A2H", "1A2I",
                     "1A2J", "1A2K", "1A2L", "1A2M", "2A1", "2A2", "2A3", "2A4A", 
                     "2A4B", "2A4C", "2A4D", "2B1", "2B2", "2B3", "2B4", "2B5",
                     "2B6", "2B7", "2B9A", "2B9B", "2B10", "2C1", "2C2", "2C3",
                     "2C5", "2D1", "2D2", "2D3", "2D4", "2E"]
    
    ## Fuel
    sgp_tax_fuel_I = ["Coal/peat", "Oil", "Natural gas"]    
    
    ## Coverage dictionaries
    sgp_tax_jur_coverage = {2019:sgp_tax_jur_I, 2020:sgp_tax_jur_I,
                           2021:sgp_tax_jur_I}
    
    sgp_tax_ipcc_coverage = {2019:sgp_tax_ipcc_I, 2020:sgp_tax_ipcc_I,
                            2021:sgp_tax_ipcc_I}     

    sgp_tax_fuel_coverage = {2019:sgp_tax_fuel_I, 2020:sgp_tax_fuel_I,
                            2021:sgp_tax_fuel_I}     
    
    ## Sources dictionary
    
    sgp_tax_coverage_sources = {2019:"leg(SG[2018])", 2020:"leg(SG[2018])",
                                2021:"leg(SG[2018])"}
    
    #----------------------------------------------------------------------------

    # Slovenia
    
    ## Jurisdictions    
    
    slo_tax_jur_I = ["Slovenia"]
    
    ## Sectors
    slo_tax_ipcc_I = ["1A1A2", "1A1A3", "1A1B", "1A1C", 
                      "1A2A", "1A2B", "1A2C", "1A2D", "1A2E", "1A2F", "1A2G", 
                      "1A2H", "1A2I", "1A2J", "1A2K", "1A2L", "1A2M", 
                      "1A4B", "1A4C1", "1A4C2", "4C1"]
    
    
    ## Fuels

    slo_tax_I_fuel_I = ["Oil", "Coal/peat", "Natural gas"]      
    
    ## Coverage dictionaries

    slo_tax_jur_coverage = {1996:slo_tax_jur_I,
                            1997:slo_tax_jur_I, 1998:slo_tax_jur_I,
                            1999:slo_tax_jur_I, 2000:slo_tax_jur_I,
                            2001:slo_tax_jur_I, 2002:slo_tax_jur_I,
                            2003:slo_tax_jur_I, 2004:slo_tax_jur_I,
                            2005:slo_tax_jur_I, 2006:slo_tax_jur_I,
                            2007:slo_tax_jur_I, 2008:slo_tax_jur_I,
                            2009:slo_tax_jur_I, 2010:slo_tax_jur_I,
                            2011:slo_tax_jur_I, 2012:slo_tax_jur_I,
                            2013:slo_tax_jur_I, 2014:slo_tax_jur_I,
                            2015:slo_tax_jur_I, 2016:slo_tax_jur_I,
                            2017:slo_tax_jur_I, 2018:slo_tax_jur_I,
                            2019:slo_tax_jur_I, 2020:slo_tax_jur_I,
                            2021:slo_tax_jur_I}

    slo_tax_ipcc_coverage = {1995:slo_tax_ipcc_I, 1996:slo_tax_ipcc_I,
                             1997:slo_tax_ipcc_I, 1998:slo_tax_ipcc_I,
                             1999:slo_tax_ipcc_I, 2000:slo_tax_ipcc_I,
                             2001:slo_tax_ipcc_I, 2002:slo_tax_ipcc_I,
                             2003:slo_tax_ipcc_I, 2004:slo_tax_ipcc_I,
                             2005:slo_tax_ipcc_I, 2006:slo_tax_ipcc_I,
                             2007:slo_tax_ipcc_I, 2008:slo_tax_ipcc_I,
                             2009:slo_tax_ipcc_I, 2010:slo_tax_ipcc_I,
                             2011:slo_tax_ipcc_I, 2012:slo_tax_ipcc_I,
                             2013:slo_tax_ipcc_I, 2014:slo_tax_ipcc_I,
                             2015:slo_tax_ipcc_I, 2016:slo_tax_ipcc_I,
                             2017:slo_tax_ipcc_I, 2018:slo_tax_ipcc_I,
                             2019:slo_tax_ipcc_I, 2020:slo_tax_ipcc_I,
                             2021:slo_tax_ipcc_I}
    
    slo_tax_fuel_coverage = {1996:nor_tax_I_fuel_I,
                             1997:slo_tax_I_fuel_I, 1998:slo_tax_I_fuel_I,
                             1999:slo_tax_I_fuel_I, 2000:slo_tax_I_fuel_I,
                             2001:slo_tax_I_fuel_I, 2002:slo_tax_I_fuel_I,
                             2003:slo_tax_I_fuel_I, 2004:slo_tax_I_fuel_I,
                             2005:slo_tax_I_fuel_I, 2006:slo_tax_I_fuel_I,
                             2007:slo_tax_I_fuel_I, 2008:slo_tax_I_fuel_I,
                             2009:slo_tax_I_fuel_I, 2010:slo_tax_I_fuel_I,
                             2011:slo_tax_I_fuel_I, 2012:slo_tax_I_fuel_I,
                             2013:slo_tax_I_fuel_I, 2014:slo_tax_I_fuel_I,
                             2015:slo_tax_I_fuel_I, 2016:slo_tax_I_fuel_I,
                             2017:slo_tax_I_fuel_I, 2018:slo_tax_I_fuel_I,
                             2019:slo_tax_I_fuel_I, 2020:slo_tax_I_fuel_I,
                             2021:slo_tax_I_fuel_I}
    
    ## Sources dictionary
    
    slo_tax_coverage_sources = {1996:"leg(SLO-CO2[1996])",
                                1997:"leg(SLO-CO2[1997])", 1998:"leg(SLO-CO2[1998])",
                                1999:"leg(SLO-CO2[1998])", 2000:"leg(SLO-CO2[2000])",
                                2001:"leg(SLO-CO2[2000])", 2002:"leg(SLO-CO2[2000])",
                                2003:"leg(SLO-CO2[2000])", 2004:"leg(SLO-CO2[2000])",
                                2005:"leg(SLO-CO2[2000])", 2006:"leg(SLO-CO2[2000])",
                                2007:"leg(SLO-CO2[2006])", 2008:"leg(SLO-CO2[2008])",
                                2009:"leg(SLO-CO2[2009a])", 2010:"leg(SLO-CO2[2009b])",
                                2011:"leg(SLO-CO2[2010])", 2012:"leg(SLO-CO2[2011])",
                                2013:"leg(SLO-CO2[2012])", 2014:"leg(SLO-CO2[2013])",
                                2015:"leg(SLO-CO2[2014])", 2016:"leg(SLO-CO2[2016])",
                                2017:"leg(SLO-CO2[2016])", 2018:"leg(SLO-CO2[2018])",
                                2019:"leg(SLO-CO2[2018])", 2020:"leg(SLO-CO2[2020])",
                                2021:"leg(SLO-CO2[2020])"}
    
    #----------------------------------------------------------------------------

    # South Africa 
    
    ## Jurisdiction
    
    zaf_tax_jur_I = ["South Africa"]
    
    
    ## Sectors
    
    zaf_tax_ipcc_I = ["1A1A1", "1A1A2", "1A1A3", "1A1B", "1A1C", "1A2A", "1A2B", 
                      "1A2C", "1A2D", "1A2E", "1A2F", "1A2G", "1A2H", "1A2I", 
                      "1A2J", "1A2K", "1A2L", "1A2M", "1A3A1", "1A3A2", "1A3B", 
                      "1A3C", "1A3D", "1A3D1", "1A3D2", "1A3E", "1A3E1", "1A4A", 
                      "1A4C1", "1A4C2", "1A4C3", "1A5A", "1A5B", "1A5C", "1B1A", 
                      "1B1A1", "1B1A11", "1B1A12", "1B1A13", "1B1A14", "1B1A2", 
                      "1B1A21", "1B1A22", "1B2A1", "1B2A2", "1B2A3", "1B2A31", 
                      "1B2A32", "1B2A33", "1B2A34", "1B2A35", "1B2A36", "1B2B1", 
                      "1B2B2", "1B2B3", "1B2B31", "1B2B32", "1B2B33", "1B2B34", 
                      "1B2B35", "1B2B36", "1B3", "1C1A", "1C1B", "1C1C", "1C2A", 
                      "1C2B", "1C3", "2A1", "2A2", "2A3", "2A4", "2A4A", "2A4B", 
                      "2A4C", "2A4D", "2B1", "2B10", "2B2", "2B3", "2B4", "2B5", 
                      "2B6", "2B7", "2B8A", "2B8B", "2B8C", "2B8D", "2B8E", "2B8F", 
                      "2B9A", "2B9B", "2C1", "2C2", "2C3", "2C4", "2C5", "2C6", 
                      "2C7", "2D1", "2D2", "2D3", "2D4", "2E", "2F1", "2F2", "2F3", 
                      "2F4", "2F5", "2F6", "2G1", "2G2", "2G3", "2G4", "2H1", 
                      "2H2", "2H3", "5A1", "5A2"]
    
    ## Fuel
    zaf_tax_fuel_I = ["Coal/peat", "Oil", "Natural gas"]    
    
    ## Coverage dictionaries
    zaf_tax_jur_coverage = {2019:zaf_tax_jur_I, 2020:zaf_tax_jur_I,
                           2021:zaf_tax_jur_I}
    
    zaf_tax_ipcc_coverage = {2019:zaf_tax_ipcc_I, 2020:zaf_tax_ipcc_I,
                            2021:zaf_tax_ipcc_I}     

    zaf_tax_fuel_coverage = {2019:zaf_tax_fuel_I, 2020:zaf_tax_fuel_I,
                            2021:zaf_tax_fuel_I}     
    
    ## Sources dictionary
    
    zaf_tax_coverage_sources = {2019:"leg(SA[2019])", 2020:"leg(SA[2019])",
                                2021:"leg(SA[2019])"}
    
    #----------------------------------------------------------------------------
    
    # Spain (F-gases)
    
    
    #----------------------------------------------------------------------------

    # Sweden
    
    ## Jurisdictions    
    
    swe_tax_jur_I = ["Sweden"]
    
    ## Sectors
    swe_tax_ipcc_I = ["1A1B", "1A1C", "1A2A", "1A2B", "1A2C", "1A2D", "1A2E",
                      "1A2F", "1A2G", "1A2H", "1A2I", "1A2J", "1A2K", "1A2L",
                      "1A2M", "1A3B", "1A4A", "1A4B", "1A4C1", "1A4C2"]

    swe_tax_ipcc_II = ["1A1B", "1A1C", "1A3B", "1A4A", "1A4B", "1A4C1", 
                       "1A4C2"]

    
    ## Fuels

    swe_tax_fuel_I = ["Oil", "Coal/peat", "Natural gas"]      
    
    ## Coverage dictionaries

    swe_tax_jur_coverage = {1991:swe_tax_jur_I, 1992:swe_tax_jur_I,
                              1993:swe_tax_jur_I, 1994:swe_tax_jur_I,
                              1995:swe_tax_jur_I, 1996:swe_tax_jur_I,
                              1997:swe_tax_jur_I, 1998:swe_tax_jur_I,
                              1999:swe_tax_jur_I, 2000:swe_tax_jur_I,
                              2001:swe_tax_jur_I, 2002:swe_tax_jur_I,
                              2003:swe_tax_jur_I, 2004:swe_tax_jur_I,
                              2005:swe_tax_jur_I, 2006:swe_tax_jur_I,
                              2007:swe_tax_jur_I, 2008:swe_tax_jur_I,
                              2009:swe_tax_jur_I, 2010:swe_tax_jur_I,
                              2011:swe_tax_jur_I, 2012:swe_tax_jur_I,
                              2013:swe_tax_jur_I, 2014:swe_tax_jur_I,
                              2015:swe_tax_jur_I, 2016:swe_tax_jur_I,
                              2017:swe_tax_jur_I, 2018:swe_tax_jur_I,
                              2019:swe_tax_jur_I, 2020:swe_tax_jur_I,
                              2021:swe_tax_jur_I}

    swe_tax_ipcc_coverage = {1991:swe_tax_ipcc_I, 1992:swe_tax_ipcc_I,
                              1993:swe_tax_ipcc_I, 1994:swe_tax_ipcc_I,
                              1995:swe_tax_ipcc_I, 1996:swe_tax_ipcc_I,
                              1997:swe_tax_ipcc_I, 1998:swe_tax_ipcc_I,
                              1999:swe_tax_ipcc_I, 2000:swe_tax_ipcc_I,
                              2001:swe_tax_ipcc_I, 2002:swe_tax_ipcc_I,
                              2003:swe_tax_ipcc_I, 2004:swe_tax_ipcc_I,
                              2005:swe_tax_ipcc_I, 2006:swe_tax_ipcc_I,
                              2007:swe_tax_ipcc_I, 2008:swe_tax_ipcc_I,
                              2009:swe_tax_ipcc_I, 2010:swe_tax_ipcc_I,
                              2011:swe_tax_ipcc_II, 2012:swe_tax_ipcc_II,
                              2013:swe_tax_ipcc_II, 2014:swe_tax_ipcc_II,
                              2015:swe_tax_ipcc_II, 2016:swe_tax_ipcc_II,
                              2017:swe_tax_ipcc_II, 2018:swe_tax_ipcc_II,
                              2019:swe_tax_ipcc_II, 2020:swe_tax_ipcc_II,
                              2021:swe_tax_ipcc_II}
    
    swe_tax_fuel_coverage = {1991:swe_tax_fuel_I, 1992:swe_tax_fuel_I,
                              1993:swe_tax_fuel_I, 1994:swe_tax_fuel_I,
                              1995:swe_tax_fuel_I, 1996:swe_tax_fuel_I,
                              1997:swe_tax_fuel_I, 1998:swe_tax_fuel_I,
                              1999:swe_tax_fuel_I, 2000:swe_tax_fuel_I,
                              2001:swe_tax_fuel_I, 2002:swe_tax_fuel_I,
                              2003:swe_tax_fuel_I, 2004:swe_tax_fuel_I,
                              2005:swe_tax_fuel_I, 2006:swe_tax_fuel_I,
                              2007:swe_tax_fuel_I, 2008:swe_tax_fuel_I,
                              2009:swe_tax_fuel_I, 2010:swe_tax_fuel_I,
                              2011:swe_tax_fuel_I, 2012:swe_tax_fuel_I,
                              2013:swe_tax_fuel_I, 2014:swe_tax_fuel_I,
                              2015:swe_tax_fuel_I, 2016:swe_tax_fuel_I,
                              2017:swe_tax_fuel_I, 2018:swe_tax_fuel_I,
                              2019:swe_tax_fuel_I, 2020:swe_tax_fuel_I,
                              2021:swe_tax_fuel_I}
    
    ## Sources dictionary
    
    swe_tax_coverage_sources = {1991:"report(SMF-CT[2011])", 1992:"report(SMF-CT[2011])",
                                   1993:"report(SMF-CT[2011])", 1994:"report(SMF-CT[2011])",
                                   1995:"report(SMF-CT[2011])", 1996:"report(SMF-CT[2011])",
                                   1997:"report(SMF-CT[2011])", 1998:"report(SMF-CT[2011])",
                                   1999:"report(SMF-CT[2011])", 2000:"report(SMF-CT[2011])",
                                   2001:"report(SMF-CT[2011])", 2002:"report(SMF-CT[2011])",
                                   2003:"report(SMF-CT[2011])", 2004:"report(SMF-CT[2011])",
                                   2005:"report(SMF-CT[2011])", 2006:"report(SMF-CT[2011])",
                                   2007:"report(SMF-CT[2011])", 2008:"report(SMF-CT[2011])",
                                   2009:"report(SMF-CT[2011])", 2010:"report(SMF-CT[2011])",
                                   2011:"report(SMF-CT[2011])", 2012:"report(SMF-CT[2011])",
                                   2013:"report(SMF-CT[2011])", 2014:"report(SMF-CT[2011])",
                                   2015:"report(SMF-CT[2011])", 2016:"report(SMF-CT[2011])",
                                   2017:"report(SMF-CT[2011])", 2018:"report(SMF-CT[2011])",
                                   2019:"report(SMF-CT[2011])", 2020:"report(SMF-CT[2011])",
                                   2021:"report(SMF-CT[2011])"}

    #----------------------------------------------------------------------------

    # Switzerland
    
    ## Jurisdiction
    
    che_tax_jur_I = ["Switzerland"]

    ## Sectors
    
    # initial coverage
    che_tax_ipcc_I = ["1A1A2", "1A1A3", "1A4B"]

    ## Fuels
    
    che_tax_fuel_I = ["Oil", "Natural gas", "Coal/peat"]

    ## Coverage dictionaries
    
    che_tax_jur_coverage = {2008:che_tax_jur_I, 2009:che_tax_jur_I,
                            2010:che_tax_jur_I, 2011:che_tax_jur_I,
                            2012:che_tax_jur_I, 2013:che_tax_jur_I,
                            2014:che_tax_jur_I, 2015:che_tax_jur_I,
                            2016:che_tax_jur_I, 2017:che_tax_jur_I,
                            2018:che_tax_jur_I, 2019:che_tax_jur_I, 
                            2020:che_tax_jur_I}
    
    che_tax_ipcc_coverage = {2008:che_tax_ipcc_I, 2009:che_tax_ipcc_I,
                            2010:che_tax_ipcc_I, 2011:che_tax_ipcc_I,
                            2012:che_tax_ipcc_I, 2013:che_tax_ipcc_I,
                            2014:che_tax_ipcc_I, 2015:che_tax_ipcc_I,
                            2016:che_tax_ipcc_I, 2017:che_tax_ipcc_I,
                            2018:che_tax_ipcc_I, 2019:che_tax_ipcc_I, 
                            2020:che_tax_ipcc_I}
    
    che_tax_fuel_coverage = {2008:che_tax_fuel_I, 2009:che_tax_fuel_I,
                            2010:che_tax_fuel_I, 2011:che_tax_fuel_I,
                            2012:che_tax_fuel_I, 2013:che_tax_fuel_I,
                            2014:che_tax_fuel_I, 2015:che_tax_fuel_I,
                            2016:che_tax_fuel_I, 2017:che_tax_fuel_I,
                            2018:che_tax_fuel_I, 2019:che_tax_fuel_I, 
                            2020:che_tax_fuel_I}
    
    ## Sources dictionary
    
    che_tax_coverage_sources = {2008:"gvt(CH[2005], CH[2009])", 
                                2009:"gvt(CH[2005], CH[2009])",
                                2010:"gvt(CH[2005], CH[2009])", 
                                2011:"gvt(CH[2005], CH[2009])", 
                                2012:"gvt(CH[2005], CH[2009])",
                                2013:"gvt(CH[2005], CH[2009])", 
                                2014:"leg(CHE-CO2[2013], CHE-FARC[2013])", 
                                2015:"leg(CHE-CO2[2013], CHE-FARC[2013])", 
                                2016:"leg(CHE-CO2[2013], CHE-FARC[2013])",
                                2017:"leg(CHE-CO2[2013], CHE-FARC[2013])", 
                                2018:"leg(CHE-CO2[2013], CHE-FARC[2013])", 
                                2019:"leg(CHE-CO2[2013], CHE-FARC[2013])", 
                                2020:"leg(CHE-CO2[2013], CHE-FARC[2013])",
                                2021:"leg(CHE-CO2[2013], CHE-FARC[2013])"}

    #----------------------------------------------------------------------------
    
    # Ukraine
    
    ## Jurisdiction
    
    ukr_tax_jur_I = ["Ukraine"]

    ## Sectors
    
    # initial coverage
    ukr_tax_ipcc_I = ["1A1A1", "1A1A2", "1A1A3", "1A1B", "1A1C",
                      "1A2A", "1A2B", "1A2C", "1A2D", "1A2E", "1A2F", "1A2G", 
                      "1A2H", "1A2I", "1A2J", "1A2K", "1A2L", "1A2M",
                      "1A3A1", "1A3A2", "1A3B", "1A3C", "1A3D1", 
                      "1A3D1", "1A3D2", "1A3E1", "1A4A", "1A4B", "1A4C1",
                      "1A4C2", "1A4C3", "1A5A", "1A5B", "1A5C"]
    
    # the scheme was suspended between 2015-2016
    ukr_tax_ipcc_II = []
    
    ## Fuels
    
    ukr_tax_fuel_I = ["Oil", "Natural gas", "Coal/peat"]
    
    # the scheme was suspended between 2015-2016
    ukr_tax_fuel_II = []

    ## Coverage dictionaries
    
    ukr_tax_jur_coverage = {2011:ukr_tax_jur_I,
                            2012:ukr_tax_jur_I, 2013:ukr_tax_jur_I,
                            2014:ukr_tax_jur_I, 2015:ukr_tax_jur_I,
                            2016:ukr_tax_jur_I, 2017:ukr_tax_jur_I,
                            2018:ukr_tax_jur_I, 2019:ukr_tax_jur_I, 
                            2020:ukr_tax_jur_I}
    
    ukr_tax_ipcc_coverage = {2011:ukr_tax_ipcc_I,
                            2012:ukr_tax_ipcc_I, 2013:ukr_tax_ipcc_I,
                            2014:ukr_tax_ipcc_I, 2015:ukr_tax_ipcc_II,
                            2016:ukr_tax_ipcc_II, 2017:ukr_tax_ipcc_I,
                            2018:ukr_tax_ipcc_I, 2019:ukr_tax_ipcc_I, 
                            2020:ukr_tax_ipcc_I}
    
    ukr_tax_fuel_coverage = {2011:ukr_tax_fuel_I,
                            2012:ukr_tax_fuel_I, 2013:ukr_tax_fuel_I,
                            2014:ukr_tax_fuel_I, 2015:ukr_tax_fuel_II,
                            2016:ukr_tax_fuel_II, 2017:ukr_tax_fuel_I,
                            2018:ukr_tax_fuel_I, 2019:ukr_tax_fuel_I, 
                            2020:ukr_tax_fuel_I}
    
    ## Sources dictionary
    
    ukr_tax_coverage_sources = {2011:"leg(UA[2011], report(EBRD[2014])", 
                                2012:"leg(UA[2011], report(EBRD[2014])",
                                2013:"leg(UA[2011], report(EBRD[2014])", 
                                2014:"leg(UA[2011], report(EBRD[2014])", 
                                2015:"", 2016:"",
                                2017:"leg(UA[2011], report(EBRD[2014])", 
                                2018:"leg(UA[2011], report(EBRD[2014])", 
                                2019:"leg(UA[2011], report(EBRD[2014])", 
                                2020:"leg(UA[2011], report(EBRD[2014])",
                                2021:"leg(UA[2011], report(EBRD[2014])"}
    
    #----------------------------------------------------------------------------
    
    # United Kingdom - carbon price support
    
    ## Jurisdiction
    
    gbr_tax_jur_I = ["United Kingdom"]

    ## Sectors
    
    # initial coverage
    gbr_tax_ipcc_I = ["1A1A1", "1A1A2"]


    ## Fuels
    
    gbr_tax_fuel_I = ["Oil", "Natural gas", "Coal/peat"]

    ## Coverage dictionaries
    
    gbr_tax_jur_coverage = {2013:gbr_tax_jur_I,
                            2014:gbr_tax_jur_I, 2015:gbr_tax_jur_I,
                            2016:gbr_tax_jur_I, 2017:gbr_tax_jur_I,
                            2018:gbr_tax_jur_I, 2019:gbr_tax_jur_I, 
                            2020:gbr_tax_jur_I}
    
    gbr_tax_ipcc_coverage = {2013:gbr_tax_ipcc_I,
                            2014:gbr_tax_ipcc_I, 2015:gbr_tax_ipcc_I,
                            2016:gbr_tax_ipcc_I, 2017:gbr_tax_ipcc_I,
                            2018:gbr_tax_ipcc_I, 2019:gbr_tax_ipcc_I, 
                            2020:gbr_tax_ipcc_I}
    
    gbr_tax_fuel_coverage = {2013:gbr_tax_fuel_I,
                            2014:gbr_tax_fuel_I, 2015:gbr_tax_fuel_I,
                            2016:gbr_tax_fuel_I, 2017:gbr_tax_fuel_I,
                            2018:gbr_tax_fuel_I, 2019:gbr_tax_fuel_I, 
                            2020:gbr_tax_fuel_I, 2021:gbr_tax_fuel_I}


    ## Sources dictionary
    
    gbr_tax_coverage_sources = {2013:"leg(UK[2013a], UK[2013b])", 
                                2014:"leg(UK[2013a], UK[2013b])", 
                                2015:"leg(UK[2013a], UK[2013b])", 
                                2016:"leg(UK[2013a], UK[2013b])",
                                2017:"leg(UK[2013a], UK[2013b])", 
                                2018:"leg(UK[2013a], UK[2013b])", 
                                2019:"leg(UK[2013a], UK[2013b])", 
                                2020:"leg(UK[2013a], UK[2013b])",
                                2021:"leg(UK[2013a], UK[2013b])"}
    
    #----------------------------------------------------------------------------
    
    # Canada Federal Charge for most provinces
    
    ## Jurisdiction
    
    # initial province coverage (2019)    
    can_tax_I_jur_I = ["Manitoba", "Ontario", "Saskatchewan", "New Brunswick"]

    # New Brunswick opts out and Alberta joins in (2020-2021)
    can_tax_I_jur_II = ["Manitoba", "Ontario", "Saskatchewan", "Alberta"]

    ## Sectors
    
    can_tax_I_ipcc_I = ["1A1A3", "1A1B", "1A1C", "1A2G", "1A2H", "1A2J", "1A2K", 
                       "1A2L", "1A2M", "1A3A2", "1A3B", "1A3C", "1A3D1", 
                       "1A3D2", "1A3E1", "1A4A", "1A4B", "1A5A", "1A5B", 
                       "1A5C"]

    ## Fuels
    
    can_tax_I_fuel_I = ["Oil", "Natural gas", "Coal/peat"]

    ## Coverage dictionaries
    
    can_tax_I_jur_coverage = {2019:can_tax_I_jur_I, 2020:can_tax_I_jur_II,
                             2021:can_tax_I_jur_II}
    
    can_tax_I_ipcc_coverage = {2019:can_tax_I_ipcc_I, 2020:can_tax_I_ipcc_I,
                             2021:can_tax_I_ipcc_I}
    
    can_tax_I_fuel_coverage = {2019:can_tax_I_fuel_I, 2020:can_tax_I_fuel_I,
                             2021:can_tax_I_fuel_I}

    ## Sources dictionary
    
    can_tax_I_coverage_sources = {2019:"gvt(ECCC[2019])", 2020:"gvt(ECCC[2019])", 
                                  2021:"gvt(ECCC[2019])"}
    
    #----------------------------------------------------------------------------
    
    # Canada Federal Charge for Yukon and Nunavut
    
    ## Jurisdiction
    
    can_tax_II_jur_I = ["Yukon", "Nunavut"]

    ## Sectors
    
    # excluding aviation fuels
    can_tax_II_ipcc_I = ["1A1A3", "1A1B", "1A1C", "1A2G", "1A2H", "1A2J", "1A2K", 
                       "1A2L", "1A2M", "1A3B", "1A3C", "1A3D1", "1A3D2", 
                       "1A3E1", "1A4A", "1A4B", "1A5A", "1A5B", "1A5C"]

    ## Fuels
    
    can_tax_II_fuel_I = ["Oil", "Natural gas", "Coal/peat"]

    ## Coverage dictionaries
    
    can_tax_II_jur_coverage = {2019:can_tax_II_jur_I, 2020:can_tax_II_jur_I,
                             2021:can_tax_II_jur_I}
    
    can_tax_II_ipcc_coverage = {2019:can_tax_II_ipcc_I, 2020:can_tax_II_ipcc_I,
                             2021:can_tax_II_ipcc_I}
    
    can_tax_II_fuel_coverage = {2019:can_tax_II_fuel_I, 2020:can_tax_II_fuel_I,
                             2021:can_tax_II_fuel_I}

    ## Sources dictionary
    
    can_tax_II_coverage_sources = {2019:"gvt(ECCC[2019])", 2020:"gvt(ECCC[2019])", 
                                   2021:"gvt(ECCC[2019])"}
    
    #----------------------------------------------------------------------------
    
    # Alberta
    
    ## Jurisdiction
    
    can_ab_tax_jur_I = ["Alberta"]

    ## Sectors (2017-2019)
    
    can_ab_tax_ipcc_I = ["1A1A1", "1A1A2", "1A1A3", "1A2A", "1A2B", "1A2C", "1A2D", 
                         "1A2E", "1A2F", "1A2G", "1A2H", "1A2I", "1A2J", "1A2K", 
                         "1A2L", "1A2M", "1A3B", "1A3D1", "1A3D2", 
                         "1A3E1", "1A4A", "1A4B", "1A4C1", "1A4C2", "1A4C3", "1A5A", 
                         "1A5B", "1A5C"]

    ## Fuels
    
    can_ab_tax_fuel_I = ["Oil", "Natural gas", "Coal/peat"]

    ## Coverage dictionaries
    
    can_ab_tax_jur_coverage = {2017:can_ab_tax_jur_I, 2018:can_ab_tax_jur_I, 
                               2019:can_ab_tax_jur_I}
    
    can_ab_tax_ipcc_coverage = {2017:can_ab_tax_ipcc_I, 2018:can_ab_tax_ipcc_I, 
                                2019:can_ab_tax_ipcc_I}
    
    can_ab_tax_fuel_coverage = {2017:can_ab_tax_fuel_I, 2018:can_ab_tax_fuel_I,
                                2019:can_ab_tax_fuel_I}

    ## Sources dictionary
    
    can_ab_tax_coverage_sources = {2017:"web(ALB[2019], AG-CLR[2018]), gvt(ALB-FP[2016])", 
                                   2018:"web(ALB[2019], AG-CLR[2018]), gvt(ALB-FP[2016])", 
                                   2019:"web(ALB[2019], AG-CLR[2018]), gvt(ALB-FP[2016])"}
    
    #----------------------------------------------------------------------------
    
    # New Brunswick
    
    ## Jurisdiction
    
    can_nb_tax_jur_I = ["New Brunswick"]

    ## Sectors (2020-2021)
    
    can_nb_tax_ipcc_I = ["1A1A1", "1A1A2", "1A1A3", "1A1B", "1A1C", "1A3B", "1A3C", 
                         "1A3D1", "1A3D2", "1A3E1", "1A4A", "1A4B", 
                         "1A5A", "1A5B", "1A5C"]

    ## Fuels
    
    can_nb_tax_fuel_I = ["Oil", "Natural gas", "Coal/peat"]

    ## Coverage dictionaries
    
    can_nb_tax_jur_coverage = {2020:can_nb_tax_jur_I, 2021:can_nb_tax_jur_I}
    
    can_nb_tax_ipcc_coverage = {2020:can_nb_tax_ipcc_I, 2021:can_nb_tax_ipcc_I}
    
    can_nb_tax_fuel_coverage = {2020:can_nb_tax_fuel_I, 2021:can_nb_tax_fuel_I}

    ## Sources dictionary
    
    can_nb_tax_coverage_sources = {2020:"gvt(ECCC[2021]), report(KPMG[2020])", 
                                   2021:"gvt(ECCC[2021]), report(KPMG[2020])"}
    
    #----------------------------------------------------------------------------
    
    # Prince Edward Island
    
    ## Jurisdiction
    
    can_pe_tax_jur_I = ["Prince Edward Island"]

    ## Sectors
    
    can_pe_tax_ipcc_I = ["1A1A1", "1A1A2", "1A1A3", "1A1B", "1A1C", "1A2A", "1A2B", 
                         "1A2C", "1A2D", "1A2E", "1A2F", "1A2G", "1A2H", "1A2I", 
                         "1A2J", "1A2K", "1A2L", "1A2M", "1A3A2", "1A3B", "1A3C", 
                         "1A3D2", "1A3E1", "1A4A", "1A4B", "1A5A", 
                         "1A5B", "1A5C"]

    ## Fuels
    
    can_pe_tax_fuel_I = ["Oil", "Natural gas", "Coal/peat"]

    ## Coverage dictionaries
    
    can_pe_tax_jur_coverage = {2019:can_pe_tax_jur_I, 2020:can_pe_tax_jur_I, 
                               2021:can_pe_tax_jur_I}
    
    can_pe_tax_ipcc_coverage = {2019:can_pe_tax_ipcc_I, 2020:can_pe_tax_ipcc_I, 
                                2021:can_pe_tax_ipcc_I}
    
    can_pe_tax_fuel_coverage = {2019:can_pe_tax_fuel_I, 2020:can_pe_tax_fuel_I, 
                                2021:can_pe_tax_fuel_I}

    ## Sources dictionary
    
    can_pe_tax_coverage_sources = {2019:"gvt(ECCC[2021], PEI[2018])", 
                                   2020:"gvt(ECCC[2021], PEI[2018])", 
                                   2021:"gvt(ECCC[2021], PEI[2018])"}
    
    #----------------------------------------------------------------------------
    
    # Newfoundland and Labrador
    
    ## Jurisdiction
    
    can_nl_tax_jur_I = ["Newfoundland and Labrador"]

    ## Sectors
    
    can_nl_tax_ipcc_I = ["1A1A1", "1A1A2", "1A1A3", "1A1B", "1A1C", "1A2A", "1A2B", 
                         "1A2C", "1A2D", "1A2E", "1A2F", "1A2H", "1A2J", "1A2K", 
                         "1A2L", "1A2M", "1A3B", "1A3C", "1A3D1", "1A3D2", 
                         "1A3E1", "1A5A", "1A5B", "1A5C"]

    ## Fuels
    
    can_nl_tax_fuel_I = ["Oil", "Natural gas", "Coal/peat"]

    ## Coverage dictionaries
    
    can_nl_tax_jur_coverage = {2019:can_nl_tax_jur_I, 2020:can_nl_tax_jur_I, 
                               2021:can_nl_tax_jur_I}
    
    can_nl_tax_ipcc_coverage = {2019:can_nl_tax_ipcc_I, 2020:can_nl_tax_ipcc_I, 
                                2021:can_nl_tax_ipcc_I}
    
    can_nl_tax_fuel_coverage = {2019:can_nl_tax_fuel_I, 2020:can_nl_tax_fuel_I, 
                                2021:can_nl_tax_fuel_I}

    ## Sources dictionary
    
    can_nl_tax_coverage_sources = {2019:"leg(NL[2011])", 2020:"leg(NL[2011])", 
                                   2021:"leg(NL[2011])"}
    
    #----------------------------------------------------------------------------
    
    # Northwest Territories
    
    ## Jurisdiction
    
    can_nt_tax_jur_I = ["Northwest Territories"]

    ## Sectors
    
    can_nt_tax_ipcc_I = ["1A1A1", "1A1A2", "1A1A3", "1A1B", "1A1C", "1A2A", "1A2B", 
                         "1A2C", "1A2D", "1A2E", "1A2F", "1A2G", "1A2H", "1A2I", 
                         "1A2K", "1A2L", "1A2M", "1A3B", "1A3C", "1A3D1", 
                         "1A3D2", "1A3E1", "1A4A", "1A4B", "1A4C1", 
                         "1A4C2", "1A4C3", "1A5A", "1A5B", "1A5C"]

    ## Fuels
    
    can_nt_tax_fuel_I = ["Oil", "Natural gas", "Coal/peat"]

    ## Coverage dictionaries
    
    can_nt_tax_jur_coverage = {2019:can_nt_tax_jur_I, 2020:can_nt_tax_jur_I, 
                               2021:can_nt_tax_jur_I}
    
    can_nt_tax_ipcc_coverage = {2019:can_nt_tax_ipcc_I, 2020:can_nt_tax_ipcc_I, 
                                2021:can_nt_tax_ipcc_I}
    
    can_nt_tax_fuel_coverage = {2019:can_nt_tax_fuel_I, 2020:can_nt_tax_fuel_I, 
                                2021:can_nt_tax_fuel_I}

    ## Sources dictionary
    
    can_nt_tax_coverage_sources = {2019:"gvt(NWT[2020], ECCC[2021])", 
                                   2020:"gvt(NWT[2020], ECCC[2021])", 
                                   2021:"gvt(NWT[2020], ECCC[2021])"}


    #------------------------------All schemes dictionaries--------------------------------#

    taxes_coverage = {"arg_tax":{"jurisdictions":arg_tax_jur_coverage, 
                                  "sectors":arg_tax_ipcc_coverage,
                                  "fuels":arg_tax_fuel_coverage}, 
                      "aus_tax":{"jurisdictions":aus_tax_jur_coverage, 
                                  "sectors":aus_tax_ipcc_coverage,
                                  "fuels":aus_tax_fuel_coverage}, 
                      "chl_tax":{"jurisdictions":chl_tax_jur_coverage, 
                                  "sectors":chl_tax_ipcc_coverage,
                                  "fuels":chl_tax_fuel_coverage},
                      "che_tax":{"jurisdictions":che_tax_jur_coverage, 
                                  "sectors":che_tax_ipcc_coverage,
                                  "fuels":che_tax_fuel_coverage},                      
                      "col_tax":{"jurisdictions":col_tax_jur_coverage, 
                                  "sectors":col_tax_ipcc_coverage,
                                  "fuels":col_tax_fuel_coverage},
                      "dnk_tax":{"jurisdictions":dnk_tax_jur_coverage, 
                                  "sectors":dnk_tax_ipcc_coverage,
                                  "fuels":dnk_tax_fuel_coverage},
                      "est_tax":{"jurisdictions":est_tax_jur_coverage, 
                                  "sectors":est_tax_ipcc_coverage,
                                  "fuels":est_tax_fuel_coverage},
                      "fin_tax":{"jurisdictions":fin_tax_jur_coverage, 
                                  "sectors":fin_tax_ipcc_coverage,
                                  "fuels":fin_tax_fuel_coverage},
                      "fra_tax":{"jurisdictions":fra_tax_jur_coverage, 
                                  "sectors":fra_tax_ipcc_coverage,
                                  "fuels":fra_tax_fuel_coverage},
                      "isl_tax":{"jurisdictions":isl_tax_jur_coverage, 
                                  "sectors":isl_tax_ipcc_coverage,
                                  "fuels":isl_tax_fuel_coverage},
                      "irl_tax":{"jurisdictions":irl_tax_jur_coverage, 
                                  "sectors":irl_tax_ipcc_coverage,
                                  "fuels":irl_tax_fuel_coverage},
                      "jpn_tax":{"jurisdictions":jpn_tax_jur_coverage, 
                                  "sectors":jpn_tax_ipcc_coverage,
                                  "fuels":jpn_tax_fuel_coverage},
                      "lva_tax":{"jurisdictions":lva_tax_jur_coverage, 
                                  "sectors":lva_tax_ipcc_coverage,
                                  "fuels":lva_tax_fuel_coverage},
                      "lie_tax":{"jurisdictions":lie_tax_jur_coverage, 
                                  "sectors":lie_tax_ipcc_coverage,
                                  "fuels":lie_tax_fuel_coverage},
                      "nor_tax_I":{"jurisdictions":nor_tax_I_jur_coverage, 
                                  "sectors":nor_tax_I_ipcc_coverage,
                                  "fuels":nor_tax_I_fuel_coverage},
                      "nor_tax_II":{"jurisdictions":nor_tax_II_jur_coverage, 
                                  "sectors":nor_tax_II_ipcc_coverage,
                                  "fuels":nor_tax_II_fuel_coverage},
                      "mex_tax":{"jurisdictions":mex_tax_jur_coverage, 
                                  "sectors":mex_tax_ipcc_coverage,
                                  "fuels":mex_tax_fuel_coverage},
                      "prt_tax":{"jurisdictions":prt_tax_jur_coverage, 
                                  "sectors":prt_tax_ipcc_coverage,
                                  "fuels":prt_tax_fuel_coverage},
                      "pol_tax":{"jurisdictions":pol_tax_jur_coverage, 
                                  "sectors":pol_tax_ipcc_coverage,
                                  "fuels":pol_tax_fuel_coverage},                      
                      "sgp_tax":{"jurisdictions":sgp_tax_jur_coverage, 
                                  "sectors":sgp_tax_ipcc_coverage,
                                  "fuels":sgp_tax_fuel_coverage},
                      "swe_tax":{"jurisdictions":swe_tax_jur_coverage, 
                                  "sectors":swe_tax_ipcc_coverage,
                                  "fuels":swe_tax_fuel_coverage},
                      "slo_tax":{"jurisdictions":slo_tax_jur_coverage, 
                                  "sectors":slo_tax_ipcc_coverage,
                                  "fuels":slo_tax_fuel_coverage},
                      "zaf_tax":{"jurisdictions":zaf_tax_jur_coverage, 
                                  "sectors":zaf_tax_ipcc_coverage,
                                  "fuels":zaf_tax_fuel_coverage},
                      "ukr_tax":{"jurisdictions":ukr_tax_jur_coverage, 
                                  "sectors":ukr_tax_ipcc_coverage,
                                  "fuels":ukr_tax_fuel_coverage},
                      "gbr_tax":{"jurisdictions":gbr_tax_jur_coverage, 
                                  "sectors":gbr_tax_ipcc_coverage,
                                  "fuels":gbr_tax_fuel_coverage},
                      "can_tax_I":{"jurisdictions":can_tax_I_jur_coverage, 
                                  "sectors":can_tax_I_ipcc_coverage,
                                  "fuels":can_tax_I_fuel_coverage},
                      "can_tax_II":{"jurisdictions":can_tax_II_jur_coverage, 
                                  "sectors":can_tax_II_ipcc_coverage,
                                  "fuels":can_tax_II_fuel_coverage},
                      "can_ab_tax":{"jurisdictions":can_ab_tax_jur_coverage, 
                                  "sectors":can_ab_tax_ipcc_coverage,
                                  "fuels":can_ab_tax_fuel_coverage},
                      "can_bc_tax":{"jurisdictions":can_bc_tax_jur_coverage, 
                                  "sectors":can_bc_tax_ipcc_coverage,
                                  "fuels":can_bc_tax_fuel_coverage},
                      "can_nb_tax":{"jurisdictions":can_nb_tax_jur_coverage, 
                                  "sectors":can_nb_tax_ipcc_coverage,
                                  "fuels":can_nb_tax_fuel_coverage},
                      "can_pe_tax":{"jurisdictions":can_pe_tax_jur_coverage, 
                                  "sectors":can_pe_tax_ipcc_coverage,
                                  "fuels":can_pe_tax_fuel_coverage},
                      "can_nl_tax":{"jurisdictions":can_nl_tax_jur_coverage, 
                                  "sectors":can_nl_tax_ipcc_coverage,
                                  "fuels":can_nl_tax_fuel_coverage},
                      "can_nt_tax":{"jurisdictions":can_nt_tax_jur_coverage, 
                                  "sectors":can_nt_tax_ipcc_coverage,
                                  "fuels":can_nt_tax_fuel_coverage}}
    
    taxes_coverage_sources = {"arg_tax":arg_tax_coverage_sources,
                              "aus_tax":aus_tax_coverage_sources,
                              "che_tax":che_tax_coverage_sources,
                              "chl_tax":chl_tax_coverage_sources,
                              "col_tax":col_tax_coverage_sources,
                              "dnk_tax":dnk_tax_coverage_sources,
                              "est_tax":est_tax_coverage_sources,
                              "fin_tax":fin_tax_coverage_sources,
                              "fra_tax":fra_tax_coverage_sources,
                              "isl_tax":isl_tax_coverage_sources,
                              "irl_tax":irl_tax_coverage_sources,
                              "jpn_tax":jpn_tax_coverage_sources,
                              "lie_tax":lie_tax_coverage_sources,
                              "lva_tax":lva_tax_coverage_sources,
                              "nor_tax_I":nor_tax_I_coverage_sources,
                              "nor_tax_II":nor_tax_II_coverage_sources,
                              "mex_tax":mex_tax_coverage_sources,
                              "prt_tax":prt_tax_coverage_sources,
                              "pol_tax":pol_tax_coverage_sources,
                              "sgp_tax":sgp_tax_coverage_sources,
                              "slo_tax":slo_tax_coverage_sources,
                              "zaf_tax":zaf_tax_coverage_sources,
                              "swe_tax":swe_tax_coverage_sources,
                              "ukr_tax":ukr_tax_coverage_sources,
                              "gbr_tax":gbr_tax_coverage_sources,
                              "can_tax_I":can_tax_I_coverage_sources,
                              "can_tax_II":can_tax_II_coverage_sources,
                              "can_ab_tax":can_ab_tax_coverage_sources,
                              "can_bc_tax":can_bc_tax_coverage_sources,
                              "can_nb_tax":can_nb_tax_coverage_sources,
                              "can_pe_tax":can_pe_tax_coverage_sources,
                              "can_nl_tax":can_nl_tax_coverage_sources,
                              "can_nt_tax":can_nt_tax_coverage_sources}
    
    
    data_and_sources = {"data":taxes_coverage, "sources":taxes_coverage_sources}
    
    
    return data_and_sources
    