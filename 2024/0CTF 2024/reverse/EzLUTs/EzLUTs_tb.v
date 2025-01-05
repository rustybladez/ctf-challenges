module EzLUTs_tb();
    localparam N = 42;
    wire [0:8*N-1] flag_test = "..........................................";
    wire success;

    EzLUTs_top #(
        .N(N)
    ) inst (
        .data(flag_test),
        .success(success)
    );

    initial begin
        $dumpfile("EzLUTs.vcd");
        $dumpvars(0, EzLUTs_tb);
        #2 
        if (success) begin
            $display("Great! You've found the correct flag!");
        end
        else begin
            $display("Haha, try again!");
        end
        #2
        $finish();
    end

endmodule