#!/usr/bin/perl
my %hash;
my $ret = "True";
foreach (split('',$ARGV[0])) { $hash{$_}++; }
foreach (split('',$ARGV[1])) {
  if (exists $hash{$_} && $hash{$_}) { $hash{$_}--; } 
  else { $ret = "False"; }
}
foreach(keys %hash) { if ($hash{$_}) { $ret = "False"; } }  
printf($ret . "\n");
