

module test1
(
  x,
  y,
  s,
  clk,
  r
);

  wire __gclk__;
  wire n[5];
  wire _00_;
  wire _01_;
  wire _02_;
  wire _03_;
  wire _04_;
  wire _05_;
  wire _06_;
  wire _07_;
  wire _08_;
  wire _09_;
  wire _10_;
  wire _11_;
  wire _12_;
  wire _13_;
  wire _14_;
  wire _15_;
  wire _16_;
  wire _17_;
  wire _18_;
  input clk;
  output [3:0] r;
  input s;
  input [3:0] x;
  input [3:0] y;

  sky130_fd_sc_hd__nand2_1
  _19_
  (
    .A(x[0]),
    .B(y[0]),
    .Y(_04_)
  );


  sky130_fd_sc_hd__dlclkp
  __clockgate_cell__
  (
    .GCLK(__gclk__),
    .GATE(EN),
    .CLK(clk)
  );


  sky130_fd_sc_hd__xnor2_1
  _20_
  (
    .A(x[0]),
    .B(y[0]),
    .Y(_05_)
  );


  sky130_fd_sc_hd__nor2_1
  _21_
  (
    .A(r[0]),
    .B(s),
    .Y(_06_)
  );


  sky130_fd_sc_hd__nand2_1
  _23_
  (
    .A(x[1]),
    .B(y[1]),
    .Y(_07_)
  );


  sky130_fd_sc_hd__xnor2_1
  _24_
  (
    .A(x[1]),
    .B(y[1]),
    .Y(_08_)
  );


  sky130_fd_sc_hd__xnor2_1
  _25_
  (
    .A(_04_),
    .B(_08_),
    .Y(_09_)
  );


  sky130_fd_sc_hd__nor2_1
  _26_
  (
    .A(s),
    .B(r[1]),
    .Y(_10_)
  );


  sky130_fd_sc_hd__xor2_1
  _29_
  (
    .A(x[2]),
    .B(y[2]),
    .X(_12_)
  );


  sky130_fd_sc_hd__xnor2_1
  _30_
  (
    .A(_11_),
    .B(_12_),
    .Y(_13_)
  );


  sky130_fd_sc_hd__nor2_1
  _31_
  (
    .A(s),
    .B(r[2]),
    .Y(_14_)
  );


  sky130_fd_sc_hd__nor2_1
  _33_
  (
    .A(s),
    .B(r[3]),
    .Y(_15_)
  );


  sky130_fd_sc_hd__maj3_1
  _34_
  (
    .A(x[2]),
    .B(y[2]),
    .C(_11_),
    .X(_16_)
  );


  sky130_fd_sc_hd__xor2_1
  _35_
  (
    .A(x[3]),
    .B(y[3]),
    .X(_17_)
  );


  sky130_fd_sc_hd__xnor2_1
  _36_
  (
    .A(_16_),
    .B(_17_),
    .Y(_18_)
  );


  sky130_fd_sc_hd__inv_1
  _n1_
  (
    .A(_05_),
    .Y(n[1])
  );


  sky130_fd_sc_hd__dfxtp_1
  _38_
  (
    .CLK(__gclk__),
    .D(n[1]),
    .Q(r[0])
  );


  sky130_fd_sc_hd__inv_1
  _n2_
  (
    .A(_09_),
    .Y(n[2])
  );


  sky130_fd_sc_hd__dfxtp_1
  _39_
  (
    .CLK(__gclk__),
    .D(n[2]),
    .Q(r[1])
  );


  sky130_fd_sc_hd__inv_1
  _n3_
  (
    .A(_13_),
    .Y(n[3])
  );


  sky130_fd_sc_hd__dfxtp_1
  _40_
  (
    .CLK(__gclk__),
    .D(n[3]),
    .Q(r[2])
  );


  sky130_fd_sc_hd__inv_1
  _n4_
  (
    .A(_18_),
    .Y(n[4])
  );


  sky130_fd_sc_hd__dfxtp_1
  _41_
  (
    .CLK(__gclk__),
    .D(n[4]),
    .Q(r[3])
  );


endmodule

